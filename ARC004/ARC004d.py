# ARC004d
import sys
import math
from collections import Counter
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
MOD = 10 ** 9 + 7


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


dp = dict()


def combinations_with_replacement_countM(n, r):
    if dp.get(n) != None and dp.get(n).get(r) != None:
        return dp[n][r]
    if dp.get(n) == None:
        dp[n] = dict()
    dp[n].update({r: math.factorial(n+r-1) //
                  (math.factorial(n - 1) * math.factorial(r))})
    return dp[n][r]


ans = 1
for i in Counter(prime_factorize(abs(n))).values():
    ans = (ans*combinations_with_replacement_countM(m, i)) % MOD

print(ans*2**(m-1) % MOD)
