# ABC161c


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    n, k = map(int, input().split())
    print(min(n % k, abs(n % k-k)))


if __name__ == '__main__':
    main()
