# ARC033c
def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)

    class Bit:
        def __init__(self, n):
            self.size = n
            self.tree = [0] * (n + 1)

        def sum(self, i):
            s = 0
            while i > 0:
                s += self.tree[i]
                i -= i & -i
            return s

        def add(self, i, x):
            while i <= self.size:
                self.tree[i] += x
                i += i & -i

    q = int(input())
    BIT = Bit(10 ** 5 * 2)

    def evaluate(number):
        su = BIT.sum(number)
        if su < x:  # もっと高い値を探せ
            return 1
        # if su == x:  # まさにこの値
        #    return 0
        if su >= x:  # もっと低い値を探せ
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
                high = mid-1  # 連続値の場合mid
                highest = mid
            else:
                low = mid+1  # 連続値の場合mid
                lowest = mid

        return [lowest, highest]

    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            BIT.add(x, 1)
        else:
            num = binary_search(0, 10 ** 5 * 2 + 1)
            print(num[1])
            BIT.add(num[1], -1)


if __name__ == '__main__':
    main()
