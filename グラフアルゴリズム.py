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

# ベルマンフォード法 O(V*E)
# edges=(頂点1,頂点2,重み)


def BellmanFord(edges, num_v, source):
      # グラフの初期化
    inf = float("inf")
    dist = [inf for i in range(num_v)]
    dist[source-1] = 0

    # 辺の緩和
    for i in range(num_v):
        for edge in edges:
            if edge[0] != inf and dist[edge[1]-1] > dist[edge[0]-1] + edge[2]:
                dist[edge[1]-1] = dist[edge[0]-1] + edge[2]
                if i == num_v-1:
                    return -1

    return dist

# ワーシャルフロイド法
# Pypyで提出すること


n = 100
d = [[float("inf") for i in range(n)] for i in range(n)]
for i in range(n):
    d[i][i] = 0  # 自身のところに行くコストは０


def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


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
