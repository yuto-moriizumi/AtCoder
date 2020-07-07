# ABC173a


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    n = int(input())
    import math
    print(math.ceil(n/1000)*1000-n)


if __name__ == '__main__':
    main()
