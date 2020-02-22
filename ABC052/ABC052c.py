# ABC052c
import sys
from math import factorial
from collections import Counter
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
MOD = 10**9+7


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


ans = 1
for i in Counter(prime_factorize(factorial(n))).values():
    ans = ans*(i+1) % MOD
print(ans)
