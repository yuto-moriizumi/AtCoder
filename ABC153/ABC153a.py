# ABC153a


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    h, a = map(int, input().split())

    from math import ceil

    print(ceil(h/a))


if __name__ == '__main__':
    main()
