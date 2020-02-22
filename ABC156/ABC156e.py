# ABC156e


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと
    import math
    n, k = map(int, input().split())

    def combinations_with_replacement_count(n, r):
        return math.factorial(n+r-1) // (math.factorial(n - 1) * math.factorial(r))

    print(combinations_with_replacement_count(n, k+1))


if __name__ == '__main__':
    main()
