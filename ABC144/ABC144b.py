# ABC144b


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    # map(int,input().split())

    n = int(input())
    for i in range(1, 10):
        if n % i != 0:
            continue
        for j in range(1, 10):
            if n//i % j != 0:
                continue
            if 0 <= n//i//j <= 1:
                print('Yes')
                exit(0)
    print('No')


if __name__ == '__main__':
    main()
