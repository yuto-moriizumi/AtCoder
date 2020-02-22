def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    n, m, x = map(int, input().split())
    tree = [-1]+[int(input()) for _ in range(n)]
    move = [dict() for _ in range(n+1)]
    for _ in range(m):
        a, b, t = map(int, input().split())
        move[a].update({b: t})
        move[b].update({a: t})
    # print(move)

    # dp[i] 木iの高さ0にたどり着くまでの最短時間
    dp = [10**10]*(n+1)

    def dfs(i, t):
        if(dp[i] <= t):
            return False
        dp[i] = t
        for j in move[i].keys():
            if(move[i][j] <= tree[i]):
                dfs(j, t+move[i][j]*2)
        return True

    dfs(1, x)  # 最初は0まで下がる
    # print(dp)
    if(dp[n] == 10*10):
        print(-1)
        exit(0)
    print(dp[n]+tree[n])


if __name__ == '__main__':
    main()
