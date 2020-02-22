# ABC145e


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    n, t = map(int, input().split())
    food = [tuple(map(int, input().split())) for _ in range(n)]

    # dp[i][j][k]=j番目まで見てiを頼まずにk分以下の注文の組み合わせで最大の美味しさ
    dp = [[[0] * (t) for i in range(10)] for j in range(n + 1)]

    for i in range(n+1):
        for j in range(n):
            for k in range(t):
                if i != j and k-food[j % 10][0] >= 0:
                    dp[i][j % 10][k] = max(dp[i][j % 10][k], dp[i][(j-1) % 10]
                                           [k - food[j][0]] + food[j][1])
                dp[i][j % 10][k] = max(
                    dp[i][j % 10][k], dp[i][(j - 1) % 10][k])
    ans = 0
    for i in range(n):
        ans = max(ans, max(dp[i][(n-1) % 10]) + food[i][1])
    # print(dp)
    print(ans)


if __name__ == '__main__':
    main()
