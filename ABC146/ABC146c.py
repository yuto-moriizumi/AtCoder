# ABC146c


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    a, b, x = map(int, input().split())
    ans = 0
    left = 0
    right = min(10 ** 9 + 1, x+2)

    while (right - left > 1):
        mid = (left + right) // 2
        l = len(str(mid))
        if a * mid + b * l <= x:
            left = mid
        elif a * mid + b * l > x:
            right = mid

    if a * mid + b * l > x:
        print(mid - 1)
        exit(0)
    print(mid)


if __name__ == '__main__':
    main()
