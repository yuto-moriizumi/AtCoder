def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    n, k = map(int, input().split())
    a = []
    ruiseki = [0]
    for j in range(n):
        i = int(input())
        a.append(i)
        ruiseki.append(i+ruiseki[j])

    print(a)
    print(ruiseki)

    # dp(x,y) := x日目までに機嫌がいい日がy日あるような勝ち方のうち、勝利回数最小値
    dp = [[0]*(n+1) for _ in range(n+1)]
    dp[0][0] = 0
    dp[1][0] = 0
    dp[1][1] = 1
    ansIdx = 0
    for i in range(n):
        for j in range(n):
            ty = dp[i][j]*i
            ty = (ty/ruiseki[i+1])+1
            if(ty <= i):
                dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j]+ty)
            # same
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
            if(dp[n][ansIdx] < dp[n][j] and dp[n][j] <= k):
                ansIdx = j
    print(dp)
    print(ansIdx)


if __name__ == '__main__':
    main()
