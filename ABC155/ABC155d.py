# ABC155d


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    #b = a[n // 2:]
    #a = a[:n//2]
    print(a)
    # print(b)

    import bisect

    def evaluate(number):
        cou = 0
        for i in a:

            if i == 0:
                pos = bisect.bisect_left(a, 0)
                print(a, number, 0, pos)
                cou -= 1
            else:
                pos = bisect.bisect_left(a, number / i)
                print(a, number, number / i, pos)
                if number / i >= i:
                    cou -= 1
            cou += pos

        print(number, cou)
        if cou/2 < k:  # もっと高い値を探せ
            return 1
        if cou/2 == k:  # まさにこの値
            return 0
        if cou/2 > k:  # もっと低い値を探せ
            return - 1

    def binary_search(low, high):
        lowest = low
        highest = high
        while low <= high:  # high-low >= 10**-12 ←これ以下の誤差を許容
            mid = (low + high) // 2
            guess = evaluate(mid)
            if guess == 0:
                return [mid, mid]
            if guess < 0:
                high = mid  # 連続値の場合mid
                highest = mid
            else:
                low = mid + 1  # 連続値の場合mid
                lowest = mid

        return [lowest, highest]
    print(a[0]**2*-1, a[-1]**2)
    print(binary_search(a[0] ** 2 * -1, a[-1] ** 2))


if __name__ == '__main__':
    main()
