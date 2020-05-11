# ABC167b


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    a, b, c, k = map(int, input().split())
    at = min(a, k)
    nk = k-at
    bt = min(b, nk)
    nk = nk-bt
    ct = min(c, nk)
    print(at - ct)


if __name__ == '__main__':
    main()
