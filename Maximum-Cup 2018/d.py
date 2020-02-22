def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    n, m, l, x = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[99999]*m for _ in range(n+1)]
    # dp[i][j]=燃料をi番目までみて休憩所jに止まるのに必要な最小の周回回数
    dp[0][0] = 1
    for i in range(n+1):
        dp[i][0] = 1
    # print(dp)
    for i in range(n):
        for j in range(m):
            # print(i)
            dp[i+1][(j+a[i]) % m] = min(dp[i+1][(j+a[i]) % m],
                                        dp[i][j]+(j+a[i])/m)
    # print(dp)
    print('Yes' if dp[n][l-1] <= x else 'No')


if __name__ == '__main__':
    main()
