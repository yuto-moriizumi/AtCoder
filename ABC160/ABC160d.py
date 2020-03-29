# ABC160d


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)
    from copy import deepcopy
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    n, x, y = map(int, input().split())
    a = [[set() for i in range(n)] for j in range(n)]
    for i in range(n - 1):
        a[0][i].add(i)
        a[0][i].add(i + 1)
    a[0][n-1].add(n-1)
    a[0][x - 1].add(y - 1)
    a[0][y - 1].add(x - 1)
    ans = [0]*n
    for i in a[0]:
        ans[0] += len(i)
    # print(a)
    print(ans[0]-n-1)

    for i in range(n-2):
        for j in range(n):
            for k in a[i][j]:
                if k == j:
                    continue
                a[i + 1][j] = a[i][j].union(a[i][k])
            ans[i+1] += len(a[i + 1][j])
        print(ans[i+1]-ans[i])


if __name__ == '__main__':
    main()
