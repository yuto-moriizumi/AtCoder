# ABC147e


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    b = [list(map(int, input().split())) for _ in range(h)]

    # dp[i][j]=マスi,jでありえる赤への偏りのパターン（リスト）
    dp = [[set() for _ in range(w)] for j in range(h)]
    dp[0][0] = set([a[0][0]-b[0][0], b[0][0]-a[0][0]])

    for i in range(h):
        for j in range(w):
            for k in dp[i][j]:
                if j+1 < w:
                    nk = k + a[i][j+1] - b[i][j+1]
                    dp[i][j + 1].add(nk)
                    nk = k + b[i][j+1] - a[i][j+1]
                    dp[i][j + 1].add(nk)
                if i + 1 < h:
                    nk = k + b[i+1][j] - a[i+1][j]
                    dp[i + 1][j].add(nk)
                    nk = k + a[i+1][j] - b[i+1][j]
                    dp[i + 1][j].add(nk)
    ans = 10 ** 9
    for i in dp[h - 1][w - 1]:
        ans = min(ans, abs(i))
    print(ans)


if __name__ == '__main__':
    main()
