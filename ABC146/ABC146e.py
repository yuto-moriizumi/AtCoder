# ABC146e


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    ru = [0]
    ru2 = [0]
    for i in range(1, n+1):
        ru.append(ru[i - 1] + a[i - 1])
        ru2.append(ru[i - 1] + a[i - 1]-i)
    print(ru)
    print(ru2)

    # dp[i][j]=i-1番目の要素までで作れる部分列で余りが


if __name__ == '__main__':
    main()
