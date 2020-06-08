# ABC169c


def main():
    import sys
    import math
    from decimal import Decimal
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    a, b = map(Decimal, input().split())
    print(math.floor(a*b))


if __name__ == '__main__':
    main()
