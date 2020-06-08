# ABC006b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())
MOD = 10007
dp = [0] * 11
dp[0] = 0
dp[1] = 0
dp[2] = 1

for i in range(n):
    dp[(i + 1) % 11] += dp[i % 11] % MOD
    dp[(i + 2) % 11] += dp[i % 11] % MOD
    dp[(i + 3) % 11] += dp[i % 11] % MOD
    dp[(i-1) % 11] = 0

print(dp[(n-1) % 11] % MOD)
