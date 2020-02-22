# ARC010a
def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    n, m, a, b = map(int, input().split())
    c = [int(input()) for _ in range(m)]
    for i in range(m):
        if n <= a:
            n += b
        n -= c[i]
        if n < 0:
            print(i + 1)
            exit(0)
    print('complete')


if __name__ == '__main__':
    main()
