# ABC172c


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    memo = dict()

    def dfs(i, j, s):
        if memo.get((i, j, s)) != None:
            return memo[(i, j, s)]
        t = 0
        if i < n and s + a[i] <= k:
            t = dfs(i + 1, j, s + a[i])+1
        if j < m and s + b[j] <= k:
            t = max(t, dfs(i, j + 1, s + b[j]) + 1)
        memo[(i, j, s)] = t
        return t

    print(dfs(0, 0, 0))


if __name__ == '__main__':
    main()
