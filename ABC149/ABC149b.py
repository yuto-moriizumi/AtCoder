# ABC149b


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    a, b, k = map(int, input().split())
    nokori = k-(a-max(0, a-k))
    print(max(0, a-k), max(0, b-nokori))


if __name__ == '__main__':
    main()
