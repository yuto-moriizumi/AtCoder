# ARC098d
def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)

    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    left = 0
    while left < n:
        SUM = a[left]
        XOR = a[left]
        right = left + 1
        cnt += 1
        while right < n:
            SUM += a[right]
            XOR = XOR | a[right]
            if SUM == XOR:
                cnt += 1
                right += 1
                continue
            SUM -= a[left]
            XOR = XOR & a[left]
            left += 1
    print(cnt)


if __name__ == '__main__':
    main()
