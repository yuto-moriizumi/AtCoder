# ABC037d
def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    pat = [[-1]*w for _ in range(h)]
    # pat[i][j]=(j,i)における移動経路の総数
    d = ((0, 1), (0, -1), (1, 0), (-1, 0))
    MOD = 10**9+7

    def dfs(i, j):
        if(i < 0 or h <= i or j < 0 or w <= j):
            return 0
        if(pat[i][j] != -1):
            return pat[i][j]
        # global count
        # count += 1
        pat[i][j] = 1
        for y, x in d:
            if 0 <= i+y < h and 0 <= j+x < w and a[i][j] < a[i+y][j+x]:
                pat[i][j] += dfs(i+y, j+x)
        return pat[i][j]

    #ans = 0
    # for i in range(h):
    #    for j in range(w):
    #        ans = (ans+dfs(i, j)) % MOD
    print(sum([dfs(i, j) % MOD for i in range(h) for j in range(w)]) % MOD)
    # print(ans)
    # print(pat)
    # print(count)


if __name__ == '__main__':
    main()
