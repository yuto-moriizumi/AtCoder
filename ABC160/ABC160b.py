# ABC160b


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    x = int(input())
    print(x//500*1000+(x-x//500*500)//5*5)


if __name__ == '__main__':
    main()
