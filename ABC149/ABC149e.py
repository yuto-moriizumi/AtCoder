# ABC149e


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)

    print(input()[::-1])

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print(a)

    # dp[i][j]=i番目までのゲストでj回握手した時の最大幸福度
    # dp[i][j]=dp[i][j-1]+


if __name__ == '__main__':
    main()
