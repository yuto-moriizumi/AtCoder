# ABC156c


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    n = int(input())
    x = list(map(int, input().split()))
    import math
    cost = 10 ** 11
    for i in range(min(x), max(x) + 1):

        t = 0
        for j in x:
            t += (j - i) ** 2

        cost = min(cost, t)
        #print(i, cost)
    print(cost)


if __name__ == '__main__':
    main()
