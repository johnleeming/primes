# This is script used to assist with a listener crossword
import numpy as np
import csv

primes = [1, 2, 3, 5, 7]
roman_primes = ['I', 'II','III', 'V', 'VII']


def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num


def is_prime(num):
    i = 2
    while i <= np.sqrt(num):
        if num/i == int(num/i):
            ans = False
            break
        i += 1
        ans = True
    return ans


test = 9
while test < 5000:
    if is_prime(test):
        primes.append(test)
        roman_primes.append(int_to_roman(test))
    test += 2

with open('/home/john/primes/roman_primes.csv', 'w') as file:
    writer = csv.writer(file)
    headings = ['prime', 'roman', 'len']
    writer.writerow(headings)
    i = 0
    while i < len(primes):
        row = [primes[i], roman_primes[i], len(roman_primes[i])]
        print(row)
        writer.writerow(row)
        i += 1
