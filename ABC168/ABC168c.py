# ABC168c


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    a, b, h, m = map(int, input().split())

    hun = m / 60 * 360
    zikan = h / 12 * 360 + hun / 12
    kakudo = abs(hun - zikan)
    import math
    c = a ** 2 + b ** 2 - 2 * a * b * math.cos(kakudo * math.pi / 180)
    print(c**0.5)


if __name__ == '__main__':
    main()
