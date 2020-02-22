# ABC153b


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)

    h, n = map(int, input().split())
    a = list(map(int, input().split()))

    if sum(a) >= h:
        print('Yes')
        exit(0)
    print('No')


if __name__ == '__main__':
    main()
