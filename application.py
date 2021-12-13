import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    user_id = session.get("user_id")

    """Getting aggergated data on all stocks in transactions"""
    stocks = db.execute("SELECT symbol, SUM(quantity) FROM transactions WHERE user_id=? GROUP BY symbol", user_id)

    """Empty array for portfolio items"""
    portfolio = []
    cash = db.execute("SELECT cash FROM users WHERE id=?", user_id)
    balance = round(cash[0]["cash"], 2)
    total_portfolio_value = 0

    """Looping around all stocks that were in transactions to fill in portfolio array"""
    for stock in stocks:
        if stock["SUM(quantity)"] > 0:
            quote = lookup(stock["symbol"])
            portfolio_item = {
                "symbol": stock["symbol"],
                "quantity": stock["SUM(quantity)"],
                "price": usd(quote["price"]),
                "value": usd(quote["price"] * stock["SUM(quantity)"])
            }
            portfolio.append(portfolio_item)
            total_portfolio_value = total_portfolio_value + quote["price"] * stock["SUM(quantity)"]
            
    """Providing grand tital and balance in USD to be shown on the page"""
    grand_total = usd(balance + total_portfolio_value)
    balance = usd(balance)

    return render_template("index.html", portfolio=portfolio, balance=balance, grand_total=grand_total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":

        """Checking if the user filled in all the fields"""
        symbol = request.form.get("symbol")
        quote = lookup(symbol)
        if not symbol:
            return apology("Missing stock symbol")
        quantity = request.form.get("shares")
        if not quantity:
            return apology("Missing stock quantity")
            
        """While quantity is still a string, checking if it contains only digits"""
        
        if not quantity.isdigit():
            return apology("Invalid quantity")
        
        """Casting quantity to an int and checking if it's positive"""    
        quantity = int(request.form.get("shares"))
        
        if quantity <= 0:
            return apology("Invalid quantity")
            
        """Checking if the user provided a valid stock symbol"""
        if not quote:
            return apology("Invalid symbol")
            
            """If all data is valid, continue"""
        else:
            price = quote["price"]
            purchase = price * quantity
            user_id = session.get("user_id")
            cash = db.execute("SELECT cash FROM users WHERE id=?", user_id)

            """Checking if the user has enough cash for a purchase"""
            if (purchase > cash[0]["cash"]):
                return apology("Not enough funds to complete the purchase")
            else:

                """Updating cash amount and transactions"""
                remaining_cash = cash[0]["cash"] - purchase
                db.execute("UPDATE users SET cash=? WHERE id=?", remaining_cash, user_id)
                db.execute("INSERT INTO transactions (user_id, symbol, quantity, price, transaction_type) VALUES(?, ?, ?, ?, 'BUY')",
                            user_id, symbol, quantity, price)
                return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    user_id = session.get("user_id")
    transactions = db.execute(
        "SELECT transaction_type, symbol, quantity, price, date, time FROM transactions WHERE user_id=?", user_id)

    """Empty array of dictionaries representing transactions"""
    transaction_list = []

    """Loop around all transactions adding items to the transactions array"""
    for transaction in transactions:
        transaction_list_item = {
            "transaction_type": transaction["transaction_type"],
            "symbol": transaction["symbol"],
            "price": transaction["price"],
            "quantity": abs(transaction["quantity"]),
            "date": transaction["date"],
            "time": transaction["time"]
        }
        transaction_list.append(transaction_list_item)
    
    """Return the history page with obtained data"""
    return render_template("history.html", transaction_list=transaction_list)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":

        symbol = request.form.get("symbol")
        quote = lookup(symbol)
        
        """Check user data validity"""
        if not symbol:
            return apology("Missing stock symbol")
        elif not quote:
            return apology("Invalid symbol")
        else:
            """If the data is valid, transform the price to USD and return the /quoted template"""
            price = usd(quote["price"])
            return render_template("/quoted.html", quote=quote, price=price)

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        """Obtain the data from user and check validity"""
        
        username = request.form.get("username")
        if not username:
            return apology("Missing username")
        usernames = db.execute("SELECT username FROM users")
        for user in usernames:
            if user["username"] == username:
                return apology("Username already exists")
        password = request.form.get("password")
        if not password:
            return apology("Missing password")
        confirmation = request.form.get("confirmation")
        if not confirmation:
            return apology("Missing password confirmation")
        if not password == confirmation:
            return apology("Invalid password confirmation")
        """Hash the password and add hashed value to the database"""
        
        pwhash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, pwhash)

        return redirect("/login")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == "POST":
        """Check if all form values submitted"""

        symbol = request.form.get("symbol")
        if not symbol:
            return apology("Missing stock symbol")
        quantity = int(request.form.get("shares"))
        if not quantity:
            return apology("Missing stock quantity")
        else:

            """Get current price of the stock the user wants to sell"""
            quote = lookup(symbol)
            price = quote["price"]

            user_id = session.get("user_id")

            """Get current cash balance and current stock quantity"""
            cash = db.execute("SELECT cash FROM users WHERE id=?", user_id)
            current_quantity = db.execute(
                "SELECT SUM(quantity) FROM transactions WHERE user_id=? AND symbol=? GROUP BY symbol", user_id, symbol)
            current_quantity = current_quantity[0]

            """Check if current stock quantity is no less then the quantity the user wants to sell"""
            if (current_quantity["SUM(quantity)"] < quantity):
                return apology("Not enough shares to sell")

                """Get current price of the stock the user wants to sell"""
            else:
                remaining_cash = cash[0]["cash"] + price * quantity
                db.execute("UPDATE users SET cash=? WHERE id=?", remaining_cash, user_id)
                db.execute("INSERT INTO transactions (user_id, symbol, quantity, price, transaction_type) VALUES(?, ?, ?, ?, 'SELL')",
                            user_id, symbol, (quantity * (-1)), price)

        return redirect("/")

    else:
        user_id = session.get("user_id")
        portfolio_list = db.execute("SELECT symbol, COUNT(id) FROM transactions WHERE user_id=? GROUP BY symbol", user_id)
        stock_options = []
        """Loop over thansactions to see what stocks the user hasand add them to the stock_options array"""
        
        for item in portfolio_list:
            symbol = item["symbol"]
            stock_quantity = db.execute("SELECT SUM(quantity) FROM transactions WHERE user_id=? AND symbol=?", user_id, symbol)
            if (stock_quantity[0]["SUM(quantity)"] > 0):
                option = {
                    "symbol": item["symbol"]
                }
                stock_options.append(option)
        return render_template("sell.html", stock_options=stock_options)


@app.route("/add-funds", methods=["GET", "POST"])
@login_required
def add_funds():
    """Add funds to the account"""

    if request.method == "POST":
        """Obtain the funds amount from user and validate it"""
        funds = request.form.get("funds")
        if not funds:
            return redirect("/add-funds?status=Error")
        else:
            
            user_id = session.get("user_id")
            cash = db.execute("SELECT cash FROM users WHERE id=?", user_id)
            new_cash = float(cash[0]["cash"]) + float(funds)
            db.execute("UPDATE users SET cash=? WHERE id=?", new_cash, user_id)
            return redirect("/add-funds?status=Success")

    else:
        return render_template("add-funds.html")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
