# ABC153c


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)

    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort(reverse=True)
    print(sum(h[k:]) if k < n else 0)


if __name__ == '__main__':
    main()
