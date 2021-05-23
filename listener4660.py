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


def get_a_or_d(pair_list, a_or_d):
    ans = []
    if a_or_d == 'a':
        i = 0
    else:
        i = 1
    for p in pair_list:
        if p[i] not in ans:
            ans.append(p[i])
    return ans


#  clue tests
def ac2():
    ans = []
    i = 10000
    while i < 99999:
        g_e_pos = contains_prime(i, primes_available)
        if len(g_e_pos) > 0:
            for pos in g_e_pos:
                if i % int(pos[2]) == 0:
                    ans.append(pos)
        i += 1
    return ans


def ac7(ps):
    ans = []
    for p in ps:
        i = int(10000 / p) + 1
        pi = p * i
        while pi < 100000:
            c = contains_prime(pi, [p])
            if len(c) > 0:
                ans.extend(c)
            pi += p
    return ans


def ac11(ps, d11p):
    ans = []
    for i in range(1, 10):
        for ii in range(i + 1, 10):
            for iii in range(ii + 1, 10):
                for iv in range(iii + 1, 10):
                    test = (i * 1000) + (ii * 100) + (iii * 10) + iv
                    candidates = contains_prime(test, ps)
                    if len(candidates) > 0:
                        for c in candidates:
                            for d in d11p:
                                if (int(d[2]) % int(c[2])) == 0:
                                    ans.append(c)
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


def ac13(ps):
    ans = []
    for pp in four_digit_primes:
        candidates = contains_prime(pp, ps)
        if len(candidates) > 0:
            ans.extend(candidates)
    return ans


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


def ac18(h_pos, n_pos, w_pos):
    ans = []
    for h in h_pos:
        i = 100
        while h * i < 100000:
            c = contains_prime(h * i, n_pos)
            if len(c) > 0:
                for cc in c:
                    if len(cc[2]) == 3 and cc[2][1] == '1':
                        for p in primes_available:
                            if int(cc[2]) % p == 0:
                                cc.append(p)
                                ans.append(cc)
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


def d4(limit):
    ans = []
    for p1 in primes_available:
        i = int(10000/p1) + 1
        while p1 * i < 100000:
            candidate = contains_prime(p1 * i, primes_available)
            if len(candidate) > 0:
                for c in candidate:
                    if c[2][2] in limit and int(c[2]) in triangular_nos and int(c[1]) != p1:
                        ans.append(c)
            i += 1
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


def d10():
    i = 10000
    ans = []
    while i < 100000:
        d_sum = digit_sum(i)
        if i % d_sum == 0 and is_ascending(i):
            candidates = contains_prime(i, primes_available)
            if len(candidates) > 0:
                for c in candidates:
                    if c[2][-1] in ['8']:
                        ans.append(c)
        i += 1
    return ans


def d11(ps):
    ans = []
    for i in range(1, 10):
        for ii in range(i + 1, 10):
            for iii in range(ii + 1, 10):
                for iv in range(iii + 1, 10):
                    for v in range(iv + 1, 10):
                        test = (i * 10000) + (ii * 1000) + (iii * 100) + (iv * 10) + v
                        candidates = contains_prime(test, ps)
                        if len(candidates) > 0:
                            for c in candidates:
                                if (int(c[2]) - int(c[1])) in ps:
                                    ans.append(c)
    return ans


def d15():
    ans = []
    for t in four_digit_squares_containing_r_primes:
        if t[2][0] == '2':
            ans.append(t)
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


# main
primes = find_primes(11, 99)
primes_available = primes.copy()
r_primes = [13, 17, 31, 37, 71, 73, 79, 97]  # primes which when reversed are also prime
triangular_nos = find_tris(200)
squares = find_square(1000, 99999)
four_digit_squares = find_square(1000, 9999)
four_digit_primes = find_primes(1000, 9999)
squares_containing_primes = find_squares_containing_primes(squares, primes)
squares_containing_r_primes = find_squares_containing_primes(squares, r_primes)
four_digit_squares_containing_primes = find_squares_containing_primes(four_digit_squares, primes)
four_digit_squares_containing_r_primes = find_squares_containing_primes(four_digit_squares, r_primes)
asc_primes = find_asc_primes()

ac15_pos = ac15(primes)
print('15ac:', ac15_pos)
print('15d: ', d15())
d3_pos = find_squares_containing_primes(four_digit_squares, [73, 97])
print('3d: ', d3_pos)

primes_available.remove(17)
primes_available.remove(29)
primes_available.remove(43)

d10_pos = d10()
print('10d: ', d10_pos)
ac13_pos = ac13(primes_available)
print('13a: ', len(ac13_pos))
ac13_d10_pos = check_cross(ac13_pos, 0, d10_pos, 1)
print('13ac & 10d: ', len(ac13_d10_pos))
ac13_pos_new = get_a_or_d(ac13_d10_pos, 'a')

d6_pos = d6(primes_available)
print('6d: ', len(d6_pos))
ac5_d6_pos = check_cross(four_digit_squares_containing_r_primes, 1, d6_pos, 0)
print('5a & 6d ', len(ac5_d6_pos))
d6_pos_new = get_a_or_d(ac5_d6_pos, 'd')
print('6d: ', len(d6_pos_new))
ac13_d6_pos = check_cross(ac13_pos_new, 1, d6_pos_new, 2)
print('13ac & 6d: ', len(ac13_d6_pos))

ac2_pos = ac2()
print('2ac: ', len(ac2_pos))


d1_pos = d1(triangular_nos, primes_available)
print('d1: ', d1_pos)

ac7_pos = ac7([29])
print('7ac: ', ac7_pos)

ac18_pos = ac18([11, 13, 83, 59], asc_primes, primes_available)
print('18ac: ', len(ac18_pos))
d16_pos = d16()
print('16d: ', len(d16_pos))
ac7_d1_pos = ac7_d1(ac7_pos, d1_pos)
print('7ac & 1d: ', len(ac7_d1_pos))
ac12_pos = ac12(triangular_nos, primes_available)
print('12a: ', ac12_pos)
d4_pos = d4(['1', '8'])
print('d4: ', len(d4_pos))
ac12_d4_pos = check_cross(ac12_pos, 1, d4_pos, 2)
print('12a & d4 ', len(ac12_d4_pos))
d4_pos_new = get_a_or_d(ac12_d4_pos, 'd')
print('d4: ', len(d4_pos_new))
ac2_d4_pos = check_cross(ac2_pos, 2, d4_pos, 0)
print('2ac & 4d: ', len(ac2_d4_pos))
d11_pos = d11(primes_available)
print('11d: ', len(d11_pos))
ac11_pos = ac11(primes_available, d11_pos)
print('11ac: ', len(ac11_pos))
