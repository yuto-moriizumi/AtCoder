# ARC022b
def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)

    n = int(input())
    a = list(map(int, input().split()))
    azi = [0] * (10 ** 5 + 1)
    ans = 0

    left = 0
    cnt = 0
    right = 0
    for right in range(1, n+1):
        while left < right and azi[a[right-1] - 1] > 0:
            azi[a[left] - 1] -= 1
            cnt -= 1
            left += 1
        azi[a[right - 1] - 1] += 1
        cnt += 1
        ans = max(ans, cnt)
    print(ans)


if __name__ == '__main__':
    main()
