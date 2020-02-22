def main():
    import sys
    import math
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    n = int(input())
    a, b = map(int, input().split())
    c = int(input())
    d = [int(input()) for _ in range(n)]
    d.sort(reverse=True)
    dp = [[0]*(n+1) for _ in range(n+1)]
    # dp[i][j]=i番目までを見てj個使った時の最大カロリー

    # print(d)
    ans = c/a
    for i in range(n):
        for j in range(i+1):
            dp[i+1][j+1] = max(dp[i][j+1], dp[i][j]+d[i])
            ans = max(ans, (dp[i+1][j+1]+c)/(a+b*(j+1)))
    # print(dp)
    print(math.floor(ans))


if __name__ == '__main__':
    main()
