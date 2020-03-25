# ABC159a


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと
    import math

    def dump(*args):
        sys.stderr.write(str(args))

    def c_count(n, r):  # 組み合わせ
        if n - r < 0:
            return 0
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

    n, m = map(int, input().split())
    print(c_count(n, 2)+c_count(m, 2))


if __name__ == '__main__':
    main()
