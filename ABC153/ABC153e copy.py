# ABC153e


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)

    h, n = map(int, input().split())
    maho = []
    for _ in range(n):
        maho.append(list(map(int, input().split())))

    # dp[i][j]=i番目までの魔法でモンスターの体力をj減らすためにつかう魔力の最小値
    # dp[i][j]=min(dp[i-1][j],dp[i][j-maho[i][0]])+maho[i][1]

    dp = [[10 ** 12] * (h + 1) for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(h + 1):
            if j == 0:
                dp[i + 1][0] = 0
            dp[i + 1][j] = min(dp[i][j],
                               dp[i + 1][max(0, j - maho[i][0])] + maho[i][1])
    print(dp[n][h])


if __name__ == '__main__':
    main()
