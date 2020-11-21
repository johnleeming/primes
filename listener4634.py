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


def find_primes(biggest):
    global primes, roman_primes
    test = 9
    while test < biggest:
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


e1_c_valids = []
e1_d_valids = []
e1_n_valids = []
e1_t_valids = []
print('e1: d = Vt + c + n')
for d in primes_by_length[4]:
    for t in primes_by_length[9]:
        for c in primes_by_length[3]:
            for n in primes_by_length[6]:
                if d == ((5 * t) + c + n):
                    if d not in e1_d_valids:
                        e1_d_valids.append(d)
                    if t not in e1_t_valids:
                        e1_t_valids.append(t)
                    if c not in e1_c_valids:
                        e1_c_valids.append(c)
                    if n not in e1_n_valids:
                        e1_n_valids.append(n)
print('t: ', e1_t_valids,' d: ', e1_d_valids, ' c: ', e1_c_valids, 'n: ', e1_n_valids)

e6_s_valids = []
e6_b_valids = []
e6_t_valids = []
e6_a_valids = []
print('e6: s + b = t + a')
for s in primes_by_length[9]:
    for b in primes_by_length[2]:
        for t in e1_t_valids:
            for a in primes_by_length[2]:
                if (s + b) == (t + a):
                    if s not in e6_s_valids:
                        e6_s_valids.append(s)
                    if b not in e6_b_valids:
                        e6_b_valids.append(b)
                    if t not in e6_t_valids:
                        e6_t_valids.append(t)
                    if a not in e6_a_valids:
                        e6_a_valids.append(a)
print('s: ', e6_s_valids, ' b: ', e6_b_valids, ' t: ', e6_t_valids, ' a: ', e6_a_valids)

e3_a_valids = []
e3_m_valids = []
e3_s_valids = []
print('e3: m + IV = s + IIa')
for m in primes_by_length[5]:
    for s in e6_s_valids:
        for a in e6_a_valids:
            if (m + 4) == (s + 2 * a):
                if m not in e3_m_valids:
                    e3_m_valids.append(m)
                if s not in e3_s_valids:
                    e3_s_valids.append(s)
                if a not in e3_a_valids:
                    e3_a_valids.append(a)
print('m: ', e3_m_valids, ' s: ', e3_s_valids, ' a: ', e3_a_valids)

e6_s_valids = []
e6_b_valids = []
e6_t_valids = []
e6_a_valids = []
print('e6: s + b = t + a')
for s in e3_s_valids:
    for b in primes_by_length[2]:
        for t in e1_t_valids:
            for a in e3_a_valids:
                if (s + b) == (t + a):
                    if s not in e6_s_valids:
                        e6_s_valids.append(s)
                    if b not in e6_b_valids:
                        e6_b_valids.append(b)
                    if t not in e6_t_valids:
                        e6_t_valids.append(t)
                    if a not in e6_a_valids:
                        e6_a_valids.append(a)
print('s: ', e6_s_valids, ' b: ', e6_b_valids, ' t: ', e6_t_valids, ' a: ', e6_a_valids)

print('e2: e + f + + g + h + k + VII = s + m')
e2_valids = []
for e in primes_by_length[4]:
    for f in primes_by_length[4]:
        for g in primes_by_length[4]:
            for h in primes_by_length[4]:
                for k in primes_by_length[4]:
                    if e + f + g + h + k + 7 == e3_s_valids[0] + e6_s_valids[0]:
                        temp_valids = [e, f, g, h, k]
                        temp_valids.sort()
                        if temp_valids not in e2_valids:
                            e2_valids.append(temp_valids)
print('e, f, g, h, j, k: ', e2_valids)

print('e4: IIn = IIp + a + III')
e4_n_valids = []
e4_p_valids = []
for n in primes_by_length[6]:
    for p in primes_by_length[6]:
        if 2 * n == (2 * p) + e6_a_valids[0] + 3:
            if n not in e4_n_valids:
                e4_n_valids.append(n)
            if p not in e4_p_valids:
                e4_p_valids.append(p)
print('n: ', e4_n_valids, ' p: ', e4_p_valids)
