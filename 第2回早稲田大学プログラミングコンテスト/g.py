class Bit:  # 1-indexed
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

    def lower_bound(self, x):  # 多分O(N)くらい
        """ xを越えない最大のindexとその累積和 """
        sum_ = 0
        pos = 0
        for i in range(self.size, -1, -1):
            k = pos + (1 << i)
            if k <= self.size and sum_ + self.tree[k] < x:
                sum_ += self.tree[k]
                pos += 1 << i
        return pos + 1, sum_


n, m, h = map(int, input().split())
a = list(map(int, input().split()))
BIT = Bit(10**5*2)
for i in range(n):
    BIT.add(i+1, a[i])
index = n+1
for _ in range(m):
    o, num = input().split()
    num = int(num)
    if o == 'add':
        BIT.add(index, num)
        index += 1
    else:
        sita = BIT.lower_bound(num - h)
        ue = BIT.lower_bound(num + h)
        print(sita, ue)
        if ue[0] == sita[0]:
            BIT.add(ue[0], -1)
