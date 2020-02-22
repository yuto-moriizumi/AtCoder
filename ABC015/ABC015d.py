# ABC015d
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


W = int(input())
N, K = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0]*(W+1) for i in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K + 1):
        for k in range(W + 1):
            if k-a[i-1][0] >= 0:
                dp[i][j][k] = max(dp[i-1][j - 1]
                                  [k - a[i-1][0]] + a[i-1][1], dp[i-1][j][k])
            else:
                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k])

#print(N, K, W, len(dp))
# print(dp[N][K])
print(dp[N][K][W])
