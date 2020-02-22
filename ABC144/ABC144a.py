# ABC144a


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    a, b = map(int, input().split())
    print(a*b if max(a, b) <= 9 else -1)


if __name__ == '__main__':
    main()
