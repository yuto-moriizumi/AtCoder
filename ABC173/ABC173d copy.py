# ABC173d


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)

    def evaluate(number):
        ans = a[0]
        last1 = a[1]
        last2 = a[1]
        for i in range(2, n):
            if last1 < last2:
                ans += last2
                last2 = a[i]
            else:
                ans += last1
                last1 = a[i]
        if number < ans:  # もっと高い値を探せ
            return 1
        if number == ans:  # まさにこの値
            return 0
        if number > ans:  # もっと低い値を探せ
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
                high = mid - 1  # 連続値の場合mid
                highest = mid
            else:
                low = mid + 1  # 連続値の場合mid
                lowest = mid

        return [lowest, highest]

    print(binary_search(a[0], sum(a)))


if __name__ == '__main__':
    main()
