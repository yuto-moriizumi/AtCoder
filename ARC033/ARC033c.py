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

        def lower_bound(self, x):
            """ xを越えない最大のindexとその累積和 """
            sum_ = 0
            pos = 0
            for i in range(self.size, -1, -1):
                k = pos + (1 << i)
                if k <= self.size and sum_ + self.tree[k] < x:
                    sum_ += self.tree[k]
                    pos += 1 << i
            return pos + 1, sum_
    q = int(input())
    query = [tuple(map(int, input().split())) for _ in range(q)]

    def compr_coord(array):  # 座標圧縮 n=|array|,O(NlogN)
        toAfter = dict()
        b = [(array[i], i) for i in range(len(array))]
        b.sort()
        toBefore = [0]*(len(array)+1)
        for i in range(len(array)):
            toAfter[array[b[i][1]]] = i+1
            toBefore[i+1] = array[b[i][1]]
        return {'toBefore': toBefore, 'toAfter': toAfter}

    array = []
    for t, x in query:
        if t == 1:
            array.append(x)
    array = set(array)
    n = len(array)
    array = compr_coord(list(array))
    # print(array)

    bit = Bit(n)
    for t, x in query:
        if t == 1:
            bit.add(array['toAfter'][x], 1)
        else:
            num = bit.lower_bound(x)[0]
            print(array['toBefore'][num])
            bit.add(num, -1)


if __name__ == '__main__':
    main()
