h, w = map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(h)]

edges = []
for i in range(h):
    for j in range(1, w):
        edges.append((-(grid[i][j]*grid[i][j-1]), i*w+j, i*w+j-1))
for i in range(1, h):
    for j in range(w):
        edges.append((-(grid[i][j]*grid[i-1][j]), i*w+j, (i-1)*w+j))

#print(edges)
edges.sort()

goukei = 0
for i in grid:
    goukei += sum(i)


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


def kruskal(n, edges):  # edges: wでソート済み
    U = UnionFind(n)
    res = 0
    for e in edges:
        w, s, t = e
        if not U.same(s, t):
            res += w
            U.unite(s, t)
    return res


print(-kruskal(h*w, edges)+goukei)
