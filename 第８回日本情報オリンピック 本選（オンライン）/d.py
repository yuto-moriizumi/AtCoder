def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    h, w, n = map(int, input().split())
    grid01 = [list(map(int, input().split())) for _ in range(h)]
    dp = [[0]*(w+1) for _ in range(h+1)]
    # dp[i][j]=i+1,j+1に訪れる回数
    dp[0][0] = n

    for i in range(h):
        for j in range(w):
            if dp[i][j] % 2 == 0:
                dp[i+1][j] += dp[i][j]//2
                dp[i][j+1] += dp[i][j]//2
                continue
            dp[i+1][j] += dp[i][j]//2
            dp[i][j+1] += dp[i][j]//2
            if grid01[i][j] == 1:
                dp[i][j+1] += 1
            else:
                dp[i+1][j] += 1

    # for i in dp:
    #    print(i)

    i = j = 0
    while(i < h and j < w):
        if dp[i][j] % 2 == 0:
            if grid01[i][j] == 0:
                j += 1
            else:
                i += 1
        else:
            if grid01[i][j] == 0:
                i += 1
            else:
                j += 1
    print(i+1, j+1)


if __name__ == '__main__':
    main()
