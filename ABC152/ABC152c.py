# ABC152c


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    n = int(input())
    p = list(map(int, input().split()))

    cou = 0
    m = 10**9
    for i in range(n):
        if m < p[i]:
            cou += 1
        m = min(m, p[i])
    print(n-cou)


if __name__ == '__main__':
    main()
