# ABC167c


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    n, m, x = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    rikaido = [0]*m

    def dfs(i, su):
        if i == n:
            for al in rikaido:
                if al < x:
                    return 10 ** 12
            return su
        for j in range(m):
            rikaido[j] += a[i][j+1]
        t = dfs(i + 1, su + a[i][0])
        for j in range(m):
            rikaido[j] -= a[i][j+1]
        return min(t, dfs(i+1, su))

    ans = dfs(0, 0)

    print(ans if ans != 10 ** 12 else -1)


if __name__ == '__main__':
    main()
