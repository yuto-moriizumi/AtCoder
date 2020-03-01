# ABC157d


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    n, m, k = map(int, input().split())
    d = [[float("inf") for i in range(n)] for i in range(n)]

    for _ in range(m):
        a, b = map(int, input().split())
        d[a-1][b-1] = 1
        d[b - 1][a - 1] = 1
    block = [[False for i in range(n)] for i in range(n)]
    for _ in range(k):
        c, e = map(int, input().split())
        block[c - 1][e - 1] = True
        block[e-1][c-1] = True

    for i in range(n):
        d[i][i] = 0  # 自身のところに行くコストは０

    def warshall_floyd(d):
        #d[i][j]: iからjへの最短距離
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        return d

    warshall_floyd(d)

    for i in range(n):
        for j in 


if __name__ == '__main__':
    main()
