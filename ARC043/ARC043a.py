# ARC043a
def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)

    n, a, b = map(int, input().split())
    s = [int(input()) for _ in range(n)]
    if max(s) == min(s):
        if b != 0:
            print(-1)
            exit(0)
        p = 1
    else:
        p = b/(max(s)-min(s))
    import math
    s = [i * p for i in s]
    ca = sum(s)/n
    print(p, a - ca)


if __name__ == '__main__':
    main()
