# ABC062a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


# Union-Find木


class UnionFind:
    def __init__(self, n):
        self.tree = [i for i in range(n)]

    def root(self, x):
        if(self.tree[x] == x):
            return x
        self.tree[x] = self.root(self.tree[x])
        return self.tree[x]  # 経路圧縮

    def same(self, x, y):  # xとyが同じ木に属するか
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if(x == y):
            return
        self.tree[x] = y


uf = UnionFind(12)
uf.unite(0, 2)
uf.unite(0, 4)
uf.unite(0, 6)
uf.unite(0, 7)
uf.unite(0, 9)
uf.unite(0, 11)
uf.unite(3, 5)
uf.unite(3, 8)
uf.unite(3, 10)

x, y = map(int, input().split())
print('YNeos'[not uf.same(x-1, y-1)::2])
