# ABC154c


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    n = int(input())
    a = list(map(int, input().split()))
    b = set(a)
    if len(a) == len(b):
        print('YES')
        exit(0)
    print('NO')


if __name__ == '__main__':
    main()
