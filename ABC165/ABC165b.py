# ABC165b


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと
    import math

    def dump(*args):
        sys.stderr.write(str(args))

    x = int(input())
    now = 100

    for i in range(4000):
        if now >= x:
            print(i)
            exit(0)
        now = math.floor(now*1.01)


if __name__ == '__main__':
    main()
