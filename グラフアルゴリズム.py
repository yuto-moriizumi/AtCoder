from collections import deque
INF = 10**12


class Edge:  # 通常の辺
    def __init__(self, to, cost):
        self.to = to
        self.cost = cost


class Dijkstra:  # ダイクストラ法 O((V+E) * logV)

    def __init__(self, vCount):
        self.vCount = vCount
        self.dist = [INF for _ in range(vCount)]
        self.edges = [list() for _ in range(vCount)]
        self.q = deque()

    def calcShortest(self, start):
        self.q.append((start, 0))
        while(len(self.q) != 0):
            v, cost = self.q.popleft()  # 頂点vへのコストをcostで更新
            if self.dist[v] < cost:
                continue
            self.dist[v] = cost
            for edge in self.edges[v]:
                self.q.append((edge.to, cost+edge.cost))

    def addEdge(self, st, gl, cost):
        self.edges[st].append(Edge(gl, cost))


class BellmanFord:
    """負の辺OK"""
    class Edge:
        def __init__(self, froom, to, cost):
            self.froom = froom
            self.to = to
            self.cost = cost

    edges = set()

    def __init__(self, n):
        super().__init__()
        self.n = n

    def addEdge(self, froom, to, cost):
        self.edges.add(self.Edge(s, t, d))

    def calc(self, source):
        """O(|E||V|)"""
        # グラフの初期化
        inf = float("inf")
        dist = [inf for _ in range(self.n)]
        dist[source] = 0

        # 辺の緩和
        for i in range(self.n):
            for edge in self.edges:
                if edge.froom != inf and dist[edge.to] > dist[edge.froom] + edge.cost:
                    dist[edge.to] = dist[edge.froom] + edge.cost
                    if i == self.n-1:
                        return -1
        return dist

# ワーシャルフロイド法


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


# クラスカル法
V, E = map(int, input().split())
edges = []
for i in range(E):
    s, t, w = map(int, input().split())
    edges.append((w, s-1, t-1))
edges.sort()


def kruskal(n, edges):  # edges: wでソート済み
    U = UnionFind(n)
    res = 0
    for e in edges:
        w, s, t = e
        if not U.same(s, t):
            res += w
            U.unite(s, t)
    return res


print(kruskal(V, edges))
