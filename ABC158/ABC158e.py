# ABC158e


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    n, p = map(int, input().split())
    s = input()[:-1]
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            if i == j:
                dp[i][j] = 1 if int(s[i:j+1]) % p == 0 else 0
            elif j - i == 1:
                dp[i][j] = dp[i][j - 1] + dp[i + 1][j] + \
                    (1 if int(s[i: j + 1]) % p == 0 else 0)
            else:
                dp[i][j] = dp[i][j-1]+dp[i+1][j]-dp[i+1][j-1] + \
                    (1 if int(s[i:j+1]) % p == 0 else 0)
    print(dp[0][j])


if __name__ == '__main__':
    main()
