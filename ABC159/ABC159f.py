# ABC159f


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        if a[i] == s:
            dp[i][i] = 1
    for i in range(n):
        for j in range(i, n):
            dp[i][j] += dp[i][j-1]+dp[j][j]


if __name__ == '__main__':
    main()
