# ABC163a


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    r = int(input())
    print(r*2*3.141592653589793238)


if __name__ == '__main__':
    main()
