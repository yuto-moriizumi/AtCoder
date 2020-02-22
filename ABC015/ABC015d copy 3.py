# ABC015d
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


W = int(input())
N, K = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0]*(K+1) for i in range(W+1)] for _ in range(N+1)]

for i in range(1, N + 1):
    for j in range(1, W + 1):
        for l in range(1, K + 1):
            if (j - a[i - 1][0] >= 0):
                dp[i][j][l] = max(dp[i][j][l], dp[i-1]
                                  [j-a[i-1][0]][l-1]+a[i-1][1])
            dp[i][j][l] = max(dp[i][j][l], dp[i-1][j][l])

print(dp[N][W][K])
