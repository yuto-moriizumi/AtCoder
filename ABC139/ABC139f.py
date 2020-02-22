# ABC139f
import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

dp = [[0, 0]] * (n+1)
# print(dp)

for i in range(1, n+1):
    nx = dp[i-1][0]+xy[i-1][0]
    ny = dp[i-1][1]+xy[i-1][1]
    if (dp[i - 1][0] ** 2 + dp[i - 1][1] ** 2 < nx ** 2 + ny ** 2):
        dp[i] = [nx, ny]
    else:
        dp[i] = dp[i-1]
print(math.sqrt(dp[n][0] ** 2 + dp[n][1] ** 2))
