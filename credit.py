from cs50 import get_int

# Getting the card number from the user
card = get_int("Number: ")

luhn_num = 0
card_temp = card
total_sum_odd = 0
total_sum_even = 0
i = 0

# Counting the sum of the first group of digits multiplied by 2 (in two stages)
while card_temp != 0:
    if (i % 2) != 0:
        product_digit_sum = 0
        product = (card_temp % 10) * 2
        while product != 0:
            product_digit_sum += product % 10
            product = int(product / 10)
        total_sum_odd += product_digit_sum
    card_temp = int(card_temp / 10)
    i += 1
    
card_temp = card
i = 0

# Counting the sum of the secound group of digits
while card_temp != 0:
    if (i % 2) == 0:
        total_sum_even += card_temp % 10
    card_temp = int(card_temp / 10)
    i = i + 1

# Counting the Luhn's algorythm   
luhn_num = total_sum_odd + total_sum_even

# Determining start numbers of the card
start_numbers = int(card / 10 ** (i - 2))

# Determining the credit card type
if luhn_num % 10 != 0:
    print("INVALID")
elif (luhn_num % 10 == 0) and (i == 15) and (start_numbers == 34 or start_numbers == 37): 
    print("AMEX")
elif (luhn_num % 10 == 0) and (i == 16) and (start_numbers >= 51) and (start_numbers <= 55): 
    print("MASTERCARD")
elif (luhn_num % 10 == 0) and (i == 16 or i == 13) and (int(start_numbers / 10) == 4): 
    print("VISA")
else:
    print("INVALID")
    