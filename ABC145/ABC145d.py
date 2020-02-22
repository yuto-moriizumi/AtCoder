# ABC145d


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7-1)

    x, y = map(int, input().split())
    #dp = [[-1] * (x + 1) for _ in range(y + 1)]
    MOD = 10 ** 9 + 7
    dp2 = dict()

    def dfs(i, j):
        #print(i, j)
        if i > j*2:
            return 0
        if j > i*2:
            return 0
        if i == 0 and j == 0:
            return 1
        if i <= 0 or j <= 0:
            return 0
        if i > y or j > x:
            return 0
        if x - j > (y - i) * 2:n
            return 0
        if y - i > (x - j) * 2:
            return 0
        if dp2.get(i) == None:
            dp2[i] = dict()
        if dp2[i].get(j) == None:
            dp2[i][j] = (dfs(i - 1, j - 2) + dfs(i - 2, j - 1)) % MOD
        return dp2[i][j]
        # if dp[i][j] != -1:
        #    return dp[i][j]
        #dp[i][j] = (dfs(i - 1, j - 2) + dfs(i - 2, j - 1)) % MOD
        # return dp[i][j]

    for i in range(20, 0, -1):
        if 3 ** i > min(x, y):
            continue
        #print(y//(3**i), x//(3**i))
        dfs(y//(3**i), x//(3**i))
    print(dfs(y, x) % MOD)


if __name__ == '__main__':
    main()
