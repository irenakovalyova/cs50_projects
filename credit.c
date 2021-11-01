#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void) {
    long card = get_long("What is the card number? ");
    printf("%li\n", card);

    int luhn_num = 0;
    long card_temp = card;
    int total_sum_odd = 0;
    int total_sum_even = 0;
    int i = 0;

// Counting the sum of the first group of digits multiplied by 2 (in two stages)
    for (i = 0; card_temp != 0; i++) {
        if (i % 2 != 0) {
            int product_digit_sum = 0;
            int product = (card_temp % 10) * 2;
            for (int j = 0; product != 0; j++) {
                product_digit_sum += product % 10;
                product /= 10;
            }
            total_sum_odd += product_digit_sum;
        }
        card_temp /= 10;
    }

    card_temp = card;
    i = 0;

// Counting the sum of the secound group of digits
    for (i = 0; card_temp != 0; i++) {
        if (i % 2 == 0) {
            total_sum_even += card_temp % 10;
        }
        card_temp /= 10;
    }

// Counting the Luhn's algorythm
    luhn_num = total_sum_odd + total_sum_even;

    int start_numbers = card / (pow(10, (i - 2)));

// Determining the credit card type
    if (luhn_num % 10 != 0) {
        printf("%s\n", "INVALID");
    } else if ((luhn_num % 10 == 0) && (i == 15) && (start_numbers == 34 || start_numbers == 37)) {
        printf("%s\n", "AMERICAN EXPRESS");
    } else if ((luhn_num % 10 == 0) && (i == 16) && (start_numbers >= 51) && (start_numbers <= 55)) {
        printf("%s\n", "MASTERCARD");
    } else if ((luhn_num % 10 == 0) && (i == 16 || i == 13) && (start_numbers / 10 == 4)) {
        printf("%s\n", "VISA");
    } else {
        printf("%s\n", "INVALID");
    }
}