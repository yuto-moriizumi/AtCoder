# ARC050b
def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)

    def evaluate(n):
        r = R - n
        b = B - n
        if r < 0 or b < 0:
            return -1
        if r // (x - 1) + b // (y - 1) >= n:
            return 1
        return -1

    def binary_search(low, high):
        lowest = low
        highest = high
        while low <= high:
            mid = (low + high) // 2
            guess = evaluate(mid)
            if guess == 0:
                return [mid, mid]
            if guess < 0:
                high = mid - 1
                highest = mid
            else:
                low = mid + 1
                lowest = mid

        return [lowest, highest]

    R, B = map(int, input().split())
    x, y = map(int, input().split())
    print(binary_search(0, min(R, B))[0])


if __name__ == '__main__':
    main()
