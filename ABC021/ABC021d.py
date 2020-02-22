# ABC021d
# 重複組み合わせ


def main():
    import sys
    import math
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    n = int(input())
    k = int(input())
    MOD = 10**9+7
    #dp = [[1]*k for _ in range(n)]

    # for i in range(n-1):
    #    for j in range(k):
    #        dp[i+1][j] = (dp[i+1][j-1]+dp[i][j]) % MOD

    # print(dp[n-1][k-1])
    # print(dp)
    print(math.factorial(n+k-1) // (math.factorial(n-1) * math.factorial(k))%MOD)


if __name__ == '__main__':
    main()
