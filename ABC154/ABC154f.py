# ABC154f


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)
    import math
    # Ä‹AŠÖ”‚ğg‚í‚È‚¢ŒÀ‚èPypy‚Åo‚·‚±‚Æ
    MOD = 10**9+7
    r1, c1, r2, c2 = map(int, input().split())
    # dp[i][j]=i,j‚É‚½‚Ç‚è’…‚­ŒÂ”

    dp = dict()

    def combinations_countM(n, r):
        if dp.get(n) != None and dp.get(n).get(r) != None:
            return dp[n][r]
        if dp.get(n) == None:
            dp[n] = dict()
        dp[n].update({r: math.factorial(
            n) // (math.factorial(n - r) * math.factorial(r))})
        return dp[n][r]

    def combinations_with_replacement_count(n, r):
        return math.factorial(n+r-1) // (math.factorial(n - 1) * math.factorial(r))

    print(combinations_countM(r2 + c2, r2 - r1 + c2 - c1) % MOD)

    print(combinations_with_replacement_count(
        r2 + c2, r2 - r1 + c2 - c1) % MOD)

    #dp = [[0] * (r2+2) for _ in range(c2+2)]
    #dp[0][0] = 1
    # for i in range(c2+1):
    #    for j in range(r2+1):
    #        dp[i + 1][j] += dp[i][j]
    #        dp[i][j + 1] += dp[i][j]
    #print(*dp, sep='\n')


if __name__ == '__main__':
    main()
