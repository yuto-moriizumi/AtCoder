# ABC153f


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)
    import bisect
    from math import ceil

    n, d, a = map(int, input().split())
    mon = [list(map(int, input().split())) for _ in range(n)]
    mon.sort()
    monX = []
    for i in mon:
        monX.append(i[0])

    herasu = [0] * n
    print(monX)
    for i in range(n):
        left = bisect.bisect_left(monX, mon[i][0] - d)
        print(i, left)
        sudeni = 0
        for j in range(left, i):
            sudeni += herasu[j]
        if mon[i][1]-sudeni*a > 0:
            herasu[i] = ceil((mon[i][1] - sudeni * a) / a)

    print(herasu)


if __name__ == '__main__':
    main()
