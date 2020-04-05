# ABC161a


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    x, y, z = map(int, input().split())
    print(z, x, y)


if __name__ == '__main__':
    main()
