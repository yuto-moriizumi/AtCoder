# ABC165c
last = 0


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)
    from math import floor
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    a, b, n = map(int, input().split())

    def evaluate(number):
        return floor(a*number/b)-a*floor(number/b)
        if number < 100:  # もっと高い値を探せ
            return 1
        if number == 100:  # まさにこの値
            return 0
        if number > 100:  # もっと低い値を探せ
            return - 1

    def binary_search(low, high):
        global last
        lowest = low
        highest = high
        while low < high:  # high-low >= 10**-12 ←これ以下の誤差を許容
            mid = (low + high) // 2
            left = (low + mid) // 2
            right = (mid+high)//2
            lv = evaluate(left)
            rv = evaluate(right)
            mv = evaluate(mid)
            #print(low, high)
            if lv < rv:
                last = max(mv, rv)
                low = mid
                lowest = mid
            else:
                last = max(mv, lv)
                high = mid
                highest = mid
            continue

            if guess == 0:
                return [mid, mid]
            if guess < 0:
                high = mid - 1  # 連続値の場合mid
                highest = mid
            else:
                low = mid + 1  # 連続値の場合mid
                lowest = mid

        return [lowest, highest]

    t = binary_search(0, n + 1)[0]
    #print(t, last)
    print(max(evaluate(max(0, t-2)), evaluate(max(0, t-1)), evaluate(max(0, min(n, t))),
              evaluate(min(n, t+1)), evaluate(min(n, t+2)), last))


if __name__ == '__main__':
    main()
