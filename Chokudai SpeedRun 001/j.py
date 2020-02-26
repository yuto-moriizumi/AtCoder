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


n = int(input())
a = list(map(int, input().split()))

bit = Bit(n)

ans = 0
for i in range(n):
    ans += (i - bit.sum(a[i]))
    bit.add(a[i], 1)
print(ans)
