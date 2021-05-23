# This is script used to assist with a listener crossword
import numpy as np


#  general functions
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
    if test & 2 == 0:
        test += 1
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
    ans = True
    for i in range(1, len(ds)):
        if ds[i-1] >= ds[i]:
            ans = False
            break
    return ans


def find_asc_primes():  # find primes that have ascending digits
    ans = []
    for p in primes:
        if is_ascending(p):
            ans.append(p)
    return ans


def check_cross(a_list, a_i, d_list, d_i):
    ans = []
    for a in a_list:
        for d in d_list:
            if str(a[2])[a_i] == str(d[2])[d_i]:
                ans.append([a, d])
    return ans


#  clue tests
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
                        if str(candidate)[-1:] in limit and (100 < candidate < 999):
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
        for z in ps:
            p = t - z
            if p != z and p in ps:
                i = 2
                while p * i < 10000:
                    test = contains_prime(p * i, [p])
                    if len(test) > 0:
                        for tt in test:
                            if tt not in ans:
                                ans.append(tt)
                    i += 1
    return ans


def d10():
    i = 10000
    ans = []
    while i < 100000:
        d_sum = digit_sum(i)
        if i % d_sum == 0 and is_ascending(i):
            rp = contains_prime(i, primes)
            if len(rp) > 0:
                for a in rp:
                    if a[2][-1] in ['2', '8']:
                        ans.append(a)
        i += 1
    return ans


def d15():
    ans = []
    for t in four_digit_squares_containing_r_primes:
        if t[2][0] == '2':
            ans.append(t)
    return ans


def ac18(h_pos, n_pos, w_pos):
    ans = []
    for h in h_pos:
        i = 100
        while h * i < 100000:
            c = contains_prime(h * i, n_pos)
            if len(c) > 0:
                for cc in c:
                    if len(cc[2]) == 3 and cc[2][1] == '1':
                        for p in primes:
                            if int(cc[2]) % p == 0:
                                cc.append(p)
                                ans.append(cc)
            i += 1
    return ans


def d16():
    ans = []
    for p in primes:
        i = int(1000 / p) + 1
        while p * i < 10000:
            c = contains_prime(p * i, [p])
            if len(c) > 0:
                for cc in c:
                    if cc[0][0] == '9':
                        ans.append(cc)
            i += 1
    return ans


def ac7_d1(ac7_p, d1_p):
    ans = []
    for a in ac7_p:
        for d in d1_p:
            if str(a[2])[0] == str(d[2])[1] and [a[2], d[2]] not in ans:
                ans.append([a[2], d[2]])
    return ans


def d6(ps):
    ans = []
    for i in range(1, 9):
        for ii in range(0, 9):
            for iii in range(0, 9):
                test = (i * 10000) + (ii * 1000) + (iii * 100) + (11 * 10) + i
                candidates = contains_prime(test, ps)
                if len(candidates) > 0:
                    for c in candidates:
                        for p1 in ps:
                            if p1 != int(c[1]):
                                p2 = int(c[2]) / p1
                                if p2 % 1 == 0 and p2 != p1 and int(p2) in ps:
                                    if [str(test), c[1], c[2]] not in ans:
                                        ans.append([str(test), c[1], c[2]])
    return ans


# main
primes = find_primes(11, 99)
primes_available = primes.copy()
r_primes = [13, 17, 31, 37, 71, 73, 79, 97]  # primes which when reversed are also prime
triangular_nos = find_tris(200)
squares = find_square(1000, 99999)
four_digit_squares = find_square(1000, 9999)
four_digit_primes = find_primes(1000, 9999)
print('primes', primes)
print('triangular numbers ', triangular_nos)
print('squares ', squares)
squares_containing_primes = find_squares_containing_primes(squares, primes)
print('squares containing primes ', squares_containing_primes)
squares_containing_r_primes = find_squares_containing_primes(squares, r_primes)
print('squares containing reversible primes', squares_containing_r_primes)
four_digit_squares_containing_primes = find_squares_containing_primes(four_digit_squares, primes)
four_digit_squares_containing_r_primes = find_squares_containing_primes(four_digit_squares, r_primes)
asc_primes = find_asc_primes()
print('ascending primes ', asc_primes)
print('four digit primes ', four_digit_primes)
# ac15_pos = ac15(primes)
# print('15ac:', ac15_pos)
ac2_pos = ac2()
# print('2ac: ', ac2_pos)
primes_available.remove(17)
primes_available.remove(29)
primes_available.remove(43)
d1_pos = d1(triangular_nos, primes_available)
print('d1: ', d1_pos)
# d10_pos = d10()
# print('10d: ', d10_pos)
ac7_pos = ac7([29])
print('7ac: ', ac7_pos)
print('15d: ', d15())
ac18_pos = ac18([11, 13, 83, 59], asc_primes, primes_available)
print('18ac: ', ac18_pos)
d16_pos = d16()
print('16d: ', d16_pos)
ac7_d1_pos = ac7_d1(ac7_pos, d1_pos)
print('7ac & 1d: ', ac7_d1_pos)
ac12_pos = ac12(triangular_nos, primes_available)
print(ac12_pos)
d4_pos = d4(['1', '8'])
print('d4: ', len(d4_pos))
ac12_d4_pos = check_cross(ac12_pos, 1, d4_pos, 2)
print('12a & d4 ', len(ac12_d4_pos))
d4_pos_new = []
for pos in ac12_d4_pos:
    if pos[1] not in d4_pos_new:
        d4_pos_new.append(pos[1])
print('d4: ', len(d4_pos_new))
d6_pos = d6(primes_available)
print('6d: ', d6_pos)
ac5_d6_pos = check_cross(four_digit_squares_containing_r_primes, 1, d6_pos, 0)
print('5a & 6d ', ac5_d6_pos)
d6_pos_new = []
for pos in ac5_d6_pos:
    if pos[1] not in d6_pos_new:
        d6_pos_new.append(pos[1])
print('6d: ', d6_pos_new)
ac13_d6_pos = check_cross(four_digit_squares_containing_primes, 1, d6_pos_new, 2)
print('13A & 6d: ', ac13_d6_pos)
