# UKRAINE101
### Video Demo:  https://www.youtube.com/watch?v=IRFn9SQCzoQ
### Description: 
This is a website created with Python and Django which purpose is to improve awareness about Ukraine in other countries.
I did the MVT design pattern (Model, View, Template) which is a classic choice for Django. The entire project is managed by the manage.py file.
I also used PostgreSQL to create a database. The file urls.py provide routing between URLs and viewes these URLs are processed with.

#### PROJECT MODULES

##### Books

The books module includes two models (Comment and Book - see models.py) which represent the corresponding table in the database.
The views for this module (see views.py) are function-based which means that to display the view the program doesn't create a new object. Instead, a certain template with certain context is rendered.
The book module represents the Book Catalogue where you can find books about Ukrainian history, culture, cuisine etc.
You can add books you like to the reading list which will be available on your profile.

###### __init__.py 
Automatically generated Django file which allows to initiate the module Books.
###### admin.py 
A standard Django file for managing the admin panel for each module. In the books module it adds the Book and Category models to the admin panel.
###### apps.py 
Apps installed in the module (standard file), I didn't configure it for Books module.

###### models.py A
A file containing Django models needed to work with a database - Book and Comment model classes and methods for them.
###### tests.py
Standard file containing tests, it doesn't contain anything for the Books module.

###### views.py 
A file describing the app functionality, including book list display and book details page display.

##### Users
You can create your account a profile by registering on the website. After that, you can change anything on your profile, including password, bio, avatar etc.
The Login, Logout and Register viewes were implemented using Django's generic views as well as a generic User model.
The reading list functionality is also provided by the Users module. To implement it without page reload, I used some JavaScript (the script is in the book-details.html template).
To add fields such as avatar and bio to user profile, another model - Profile has been created (see models.py in users).

###### __init__.py 
Automatically generated Django file which allows to initiate the module Users.
###### admin.py 
A standard Django file for managing the admin panel for each module. In the books module it adds the Profile model to the admin panel.
###### apps.py 
Apps installed in the module (standard file), I didn't configure it for Users module.
###### forms.py 
A file containing form classes, including the User registration form and User login form.
###### models.py
A file containing a Profile Django model - a class to create profile objects.
###### tests.py
Standard file containing tests, it doesn't contain anything for the Users module.
###### views.py 
A file describing the app functionality, including login, logout, registration and adding a book to reading list


##### Articles
Also, there is an Articles section where ordinary users can comment (after logging in) and staff user and admins can add new articles using the admin panel (I created user groups in Django admin for that.
The Articles section's models have been implememnted using Django's generic class-based views (ListView, UpdateView) - see the file models.py.
Also, this module has a separate urls.py with URL/view routing. 
In the admin.py file you can see the admin panel for the Comment model has been customized to prevent comments from editing by anyone (to protect user privacy). The admin can only delete the comment if it violates the rules.
Each article has its own clor pallete which depends on its category. You can see how it's implemented in the Comment model (in the Books module).
Each article page provides the user with a recommended book as well as similar articles sections. They are provided based on article category.

###### __init__.py 
Automatically generated Django file which allows to initiate the module Articles.
###### admin.py 
A standard Django file for managing the admin panel for each module. In the books module it adds the Article model to the admin panel.
###### apps.py 
Apps installed in the module (standard file), I didn't configure it for Articles module.
###### forms.py 
A file containing form classes, including a form for commenting.
###### models.py
A file containing the Article Django model neeeded to work with Article objects in the database.
###### tests.py
Standard file containing tests, it doesn't contain anything for the Articles module.
###### urls.py S
Standard file for URL routing. The Article model has its own urls.py and it is added to the general on contained in the urkaine101 folder
###### views.py 
A file describing the app functionality, including article list display, article details display, commenting functionality.

##### Pages
Besides, there is a fun section called Random Fact where you can generate just a fun fact about Ukraine you certainly didn't know.
There is also a page with contacts of different charities through which anyone can donate since Ukraine needs it so much now that it is at war with Russia.

###### __init__.py 
Automatically generated Django file which allows to initiate the module Pages.
###### admin.py 
A standard Django file for managing the admin panel for each module. In the books module it adds the Fact model to the admin panel.
###### apps.py 
Apps installed in the module (standard file), I didn't configure it for Pages module.
###### models.py
A file containing the Fact model - a class needed to create and manage database objects.
###### tests.py
Standard file containing tests, it doesn't contain anything for the Articles module.
###### views.py 
A file describing the app functionality, including home page display, Support page display, and Random fact page display

##### Files and folders
static folder - CSS, JS files
media folder - images used in the project
