# ABC065c
import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
MOD = 10**9+7

if not (n == m or n == m-1 or n == m+1):
    print(0)
    exit(0)


if n == m:
    print(math.factorial(n) % MOD * math.factorial(n) % MOD * 2 % MOD)
    exit(0)
print(math.factorial(n) % MOD*math.factorial(m) % MOD)
