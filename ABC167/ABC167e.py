# ABC167e


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))
    n, m, k = map(int, input().split())
    # dp[i][j][k]=i番目までのブロックを考えるとき、

    MOD = 998244353

    dp = [[0] * (k+1) for _ in range(n+1)]
    dp[1][0] = m
    for i in range(n):
        for j in range(k+1):
            dp[i + 1][j] += dp[i][j] * (m - 1) % MOD
            if j < k:
                dp[i + 1][j + 1] += dp[i][j] % MOD
    #print(sum(dp[n]) % MOD)
    print(dp)


if __name__ == '__main__':
    main()
