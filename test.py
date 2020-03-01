
class WarshallFloyd:
    def __init__(self, n):
        super().__init__()
        self.n = n
        self.d = [[float("inf") for i in range(n)] for i in range(n)]
        for i in range(n):
            self.d[i][i] = 0  # 自身のところに行くコストは０

    def setCost(self, froom, to, cost):
        self.d[froom][to] = cost
        self.d[to][froom] = cost

    def calc(self):
        #d[i][j]: iからjへの最短距離
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    self.d[i][j] = min(
                        self.d[i][j], self.d[i][k] + self.d[k][j])
        return self.d


v, e = map(int, input().split())
tree = WarshallFloyd(v)
for _ in range(e):
    s, t, d = map(int, input().split())
    tree.setCost(s-1, t-1, d)
print(tree.calc())
