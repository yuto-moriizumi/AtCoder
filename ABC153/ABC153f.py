# ABC153f


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)
    import bisect
    from math import ceil

    def binary_search(lis, item, lh):
        low = 0
        high = len(lis) - 1

        while low <= high:
            mid = (low + high) // 2
            guess = lis[mid]
            if guess == item:
                return mid
            if guess > item:
                high = mid - 1
            else:
                low = mid + 1

        return low if lh == 0 else high

    bbb = [1, 1, 1, 1, 3, 5, 5, 6]
    print(binary_search(bbb, 3, 0))
    print(binary_search(bbb, 5, 1))

    n, d, a = map(int, input().split())
    mon = [list(map(int, input().split())) for _ in range(n)]
    mon.sort()
    herasu = []

    for i in mon:
        tairyoku = i[1]
        left = binary_search(herasu, i[0] - d)
        right = binary_search(herasu, i[0] + d)
        # for j in range(left, right):
        herasu.append((i[0], ceil(i[1] / a)))

    print(herasu)


if __name__ == '__main__':
    main()
