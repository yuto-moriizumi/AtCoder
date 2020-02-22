n, p = map(int, input().split())
a = list(map(int, input().split()))

dp = [[-1]*2 for _ in range(n)]


def use(i, j):
    if i >= n:
        return 1 if j == p else 0
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = use(i+1, j)+use(i+1, (j+a[i]) % 2)
    return dp[i][j]


print(use(0, 0))
