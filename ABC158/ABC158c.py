# ABC158c


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    a, b = map(int, input().split())
    from math import floor

    for i in range(2000):
        if floor(i * 0.08) == a and floor(i * 0.1) == b:
            print(i)
            exit(0)
    print(-1)


if __name__ == '__main__':
    main()
