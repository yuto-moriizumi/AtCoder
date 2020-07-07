# ABC173c


def main():
    import sys
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    h, w, k = map(int, input().split())
    c = [list(input()) for _ in range(h)]

    def yoko(i):
        if i >= w:
            return 1 if sum([c[i].count('#') for i in range(h)]) == k else 0
        ans = yoko(i+1)
        for j in range(h):
            t = c[j][i]
            if t == '#':
                c[j][i] = 1
            elif t == 1:
                c[j][i] = 2
        ans += yoko(i + 1)
        for j in range(h):
            t = c[j][i]
            if t == 1:
                c[j][i] = '#'
            elif t == 2:
                c[j][i] = 1
        return ans

    def tate(i):
        if i >= h:
            return yoko(0)
        ans = tate(i+1)
        for j in range(w):
            t = c[i][j]
            if t == '#':
                c[i][j] = 1
        ans += tate(i + 1)
        for j in range(w):
            t = c[i][j]
            if t == 1:
                c[i][j] = '#'
        return ans

    print(tate(0))


if __name__ == '__main__':
    main()
