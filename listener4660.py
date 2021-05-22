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


def find_square(bottom, top):
    sqs = []
    i = int(pow(bottom, 0.5)) + 1
    while i * i <= top:
        sqs.append(i * i)
        i += 1
    return sqs


def int_to_list(num):
    return list(map(int, str(num)))


def contains_prime(num, ps):
    ans = []
    t_s = str(num)
    for p in ps:
        p_s = str(p)
        i = 0
        while i < len(t_s):
            i = t_s.find(p_s, i)
            if i == -1:
                break
            candidate = t_s[:i] + t_s[i + 2:]
            if candidate[0] != '0':
                ans.append([t_s, p_s, candidate])
            i += 1
    return ans


def find_squares_containing_primes(sqs, ps):
    ans = []
    for s in sqs:
        a = contains_prime(s, ps)
        if len(a) > 0:
            ans.extend(a)
    return ans


def digitise(num):
    ds = []
    num_s = str(num)
    for c in num_s:
        ds.append(int(c))
    return ds


def digit_sum(num):
    ds = digitise(num)
    ans = 0
    for d in ds:
        ans += d
    return ans


def is_ascending(num):
    ds = digitise(num)
    ans = False
    for i in range(1,len(ds)):
        if ds[i-1] < ds[1]:
            ans = True
        else:
            ans = False
            break
    return ans


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


def d4(limit):
    pos = []
    for p1 in primes:
        i = 100
        while p1 * i < 100000:
            if p1 * i > 9999:
                t = str(p1 * i)
                for p2 in primes:
                    p2_s = str(p2)
                    ii = 0
                    while ii < len(t):
                        ii = t.find(p2_s, ii)
                        if ii == -1:
                            break
                        candidate = int(t[:ii] + t[ii + 2:])
                        if str(candidate)[-1:] in limit:
                            pos.append([str(p1 * i), p2_s, str(candidate)])
                        ii += 1
            i += 1
    return pos


def ac7(ps):
    pos = []
    for p in ps:
        p_s = str(p)
        i = 1
        pi = p * i
        while pi < 100000:
            if pi > 9999:
                t = str(pi)
                ii = 0
                while ii < len(t):
                    ii = t.find(p_s, ii)
                    if ii == -1:
                        break
                    candidate = int(t[:ii] + t[ii + 2:])
                    if candidate % p == 0 and len(str(candidate)) == 3:
                        pos.append([str(pi), p_s, str(candidate)])
                    ii += 1
            i += 1
            pi = p * i
    return pos


def ac15(ps):
    pos = []
    for p1 in ps:
        p1c_s = str(pow(p1, 3))
        for p2 in ps:
            p2_s = str(p2)
            ii = 0
            while ii < len(p1c_s):
                ii = p1c_s.find(p2_s, ii)
                if ii == -1:
                    break
                c_entry = int(p1c_s[:ii] + p1c_s[ii + 2:])
                s_pos = pow(c_entry, 1/2)
                if s_pos % 1 == 0 and is_prime(s_pos) and s_pos > 10:
                    pos.append([str(p1), p2_s, str(c_entry)])
                ii += 1
    return pos


def ac2():
    ans = []
    i = 10000
    while i < 99999:
        g_e_pos = contains_prime(i, primes)
        if len(g_e_pos) > 0:
            for pos in g_e_pos:
                if i % int(pos[2]) == 0:
                    ans.extend(pos)
        i += 1
    return ans


def d1(ts, ps):
    ans = []
    for t in ts:
        for p in ps:
            pos = t - p
            if pos != p and pos in ps:
                ans.append([pos, p, t])
    return ans


def d10():
    i = 10000
    ans = []
    while i < 100000:
        d_sum = digit_sum(i)
        if i % d_sum == 0 and is_ascending(i):
            rp = contains_prime(i, primes)
            if len(rp) > 0:
                ans.append([i, rp])
        i += 1
    return ans


# main
primes = find_primes(11, 99)
triangular_nos = find_tris(200)
squares = find_square(1000, 99999)
print(primes)
print(triangular_nos)
print(squares)
# ac12_pos = ac12(triangular_nos, primes)
# print(ac12_pos)
# d4_pos = d4(['1', '8'])
# print(d4_pos)
# ac15_pos = ac15(primes)
# print(ac15_pos)
# D_pos = []
# for pos in ac15_pos:
#     D_pos.append(int(pos[0]))
# ac7_pos = ac7(D_pos)
# print(ac7_pos)
squares_containing_primes = find_squares_containing_primes(squares, primes)
print(squares_containing_primes)
ac2_pos = ac2()
print(ac2_pos)
d1_pos = d1(triangular_nos, primes)
print(d1_pos)
d10_pos = d10()
print(d10_pos)
