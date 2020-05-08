# ABC165c


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)
    from math import floor
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    a, b, n = map(int, input().split())
    last = -1
    ans = -1

    def evaluate(number):
        return floor(a * number / b) - a * floor(number / b)

    # for i in range(1, n+1):
    #    print(i, evaluate(i))
    print(max(evaluate(min(b, n)), evaluate(min(b-1, n))))


if __name__ == '__main__':
    main()
