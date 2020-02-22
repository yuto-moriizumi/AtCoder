# ABC041b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a, b, c = map(int, input().split())
MOD = 10**9+7

print(a % MOD*b % MOD*c % MOD)
