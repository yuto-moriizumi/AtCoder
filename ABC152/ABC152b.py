# ABC152b


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)

    a = list(input().split())
    b = [a[0] * int(a[1]), a[1] * int(a[0])]
    b.sort()
    print(b[0])


if __name__ == '__main__':
    main()
