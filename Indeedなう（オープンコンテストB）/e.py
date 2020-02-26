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

if len(set(a)) != len(a):
    print(-1)
    exit(0)

b = [(a[i], i) for i in range(n)]
b.sort()

for i in range(n):
    a[b[i][1]] = (i + 1, a[b[i][1]])

bit = Bit(n)

ans = 0
for i in range(n):
    ans += (i - bit.sum(a[i][0]))*a[i][1]
    bit.add(a[i][0], 1)
print(ans)
