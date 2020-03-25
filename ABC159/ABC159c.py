# ABC159c


def main():
    import sys
    import math
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))
    l = int(input())
    print((l/3)**3)


if __name__ == '__main__':
    main()
