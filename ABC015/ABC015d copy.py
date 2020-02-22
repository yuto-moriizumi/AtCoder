# ABC015d
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


W = int(input())
N, K = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
print(a)
dp = [[[0]*(W+1) for i in range(N+1)] for _ in range(N+1)]

for i in range(N):
    for j in range(N):
        for k in range(W):
            if k+a[i][1] <= W:
                dp[i+1][j+1][k+a[i][1]] = max(dp[i][j]
                                              [k] + a[i][0], dp[i][j][k+a[i][1]])
            dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j][k])

print(N, K, W, len(dp))
print(dp)
print(dp[N][K][W])
