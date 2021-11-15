from cs50 import get_int

card = get_int("Number: ")

luhn_num = 0
card_temp = card
total_sum_odd = 0
total_sum_even = 0
i = 0

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

while card_temp != 0:
    if (i % 2) == 0:
        total_sum_even += card_temp % 10
    card_temp = int(card_temp / 10)
    i = i + 1
    
luhn_num = total_sum_odd + total_sum_even
start_numbers = int(card / 10 ** (i - 2))

if luhn_num % 10 != 0:
    print("INVALID")
elif (luhn_num % 10 == 0) and (i == 15) and (start_numbers == 34 or start_numbers == 37): 
    print("AMEX")
elif (luhn_num % 10 == 0) and (i == 16) and (start_numbers >= 51) and (start_numbers <= 55): 
    print("MASTERCARD")
elif (luhn_num % 10 == 0) and (i == 16 or i == 13) and (int(start_numbers / 10) == 4): 
    print("VISA");
else:
    print("INVALID")
    