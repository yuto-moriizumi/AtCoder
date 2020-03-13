# ABC158b


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    n, a, b = map(int, input().split())
    loo = n // (a + b)
    wa = n - loo * (a + b)
    #print(loo, wa)

    print(loo*a+min(wa, a))


if __name__ == '__main__':
    main()
