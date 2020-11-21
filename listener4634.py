# This is script used to assist with a listener crossword
import numpy as np

primes = [1, 2, 3, 5, 7]
roman_primes = ['I', 'II', 'III', 'V', 'VII']
primes_by_length = [[], [], [], [], [], [], [], [], [], []]
roman_primes_by_length = [[], [], [], [], [], [], [], [], [], []]


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
        if num / i == int(num / i):
            ans = False
            break
        i += 1
        ans = True
    return ans


def find_primes(m):
    global primes, roman_primes
    test = 9
    while test < m:
        if is_prime(test):
            primes.append(test)
            roman_primes.append(int_to_roman(test))
        test += 2
    return


def group_primes_by_length():
    global primes_by_length, roman_primes_by_length
    i = 0
    while i < len(roman_primes):
        if len(roman_primes[i]) < 10:
            primes_by_length[len(roman_primes[i])].append(primes[i])
            roman_primes_by_length[len(roman_primes[i])].append(roman_primes[i])
        i += 1
    return


# main
find_primes(5000)
group_primes_by_length()
# i = 0
# while i < 10:
#     j = 0
#     while j < len(primes_by_length[i]):
#         print(primes_by_length[i][j], roman_primes_by_length[i][j])
#         j += 1
#     i += 1

print ('e1: d = Vt + c + n')
e1_t_valids = []
for d in primes_by_length[4]:
    for t in primes_by_length[9]:
        for c in primes_by_length[3]:
            for n in primes_by_length[6]:
                if d == ((5 * t) + c + n):
                    print(d, t, c, n, int_to_roman(d), int_to_roman(t), int_to_roman(c), int_to_roman(n))
                    if t not in e1_t_valids:
                        e1_t_valids.append(t)

print(e1_t_valids)
