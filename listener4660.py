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


def find_primes(smallest, biggest):
    test = smallest
    lst = []
    while test < biggest:
        if is_prime(test):
            lst.append(test)
        test += 2
    return lst


def find_tris(num):
    ans = []
    for n in range(num):
        ans.append(int(n * (n + 1) / 2))
    return ans


def int_to_list(num):
    return list(map(int, str(num)))


def ac12(ts, ps):
    pos = []
    for t in ts:
        if 999 < t < 10000:
            t_s = str(t)
            for p in ps:
                p_s = str(p)
                i = 0
                while i < len(t_s):
                    i = t_s.find(p_s, i)
                    if i == -1:
                        break
                    candidate = int(t_s[:i] + t_s[i + 2:])
                    if candidate in ts:
                        pos.append([t_s, p_s, str(candidate)])
                    i += 1
    return pos


# main
primes = find_primes(11, 99)
triangular_nos = find_tris(200)
print(primes)
print(triangular_nos)
ac12_pos = ac12(triangular_nos, primes)
print(ac12_pos)

