# This is script used to assist with a listener crossword
import numpy as np


def is_prime(num):
    i = 2
    ans = False
    while i <= np.sqrt(num):
        if num / i == int(num / i):
            ans = False
            break
        i += 1
        ans = True
    return ans


def find_primes(biggest):
    ans = [1, 2, 3, 5, 7]
    test = 11
    while test < biggest:
        if is_prime(test):
            ans.append(test)
        test += 2
    return ans


def find_tris(num):
    ans = []
    for n in range(num):
        ans.append(int(n*(n+1)/2))
    return ans


# main
primes = find_primes(100)
triangular_nos = find_tris(20)
print(primes)
print(triangular_nos)
