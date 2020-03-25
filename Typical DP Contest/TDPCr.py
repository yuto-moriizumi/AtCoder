# 最小費用流(minimum cost flow) O(F|V||E|)
class MinCostFlow:
    def __init__(self, n):
        self.n = n
        self.G = [[] for i in range(n)]

    def addEdge(self, f, t, cap, cost):
        # [to, cap, cost, rev]
        self.G[f].append([t, cap, cost, len(self.G[t])])
        self.G[t].append([f, 0, -cost, len(self.G[f])-1])

    def minCostFlow(self, s, t, f):
        n = self.n
        G = self.G
        prevv = [0]*n
        preve = [0]*n
        INF = 10**9+7

        res = 0
        while f:
            dist = [INF]*n
            dist[s] = 0
            update = 1
            while update:
                update = 0
                for v in range(n):
                    if dist[v] == INF:
                        continue
                    gv = G[v]
                    for i in range(len(gv)):
                        to, cap, cost, rev = gv[i]
                        if cap > 0 and dist[v] + cost < dist[to]:
                            dist[to] = dist[v] + cost
                            prevv[to] = v
                            preve[to] = i
                            update = 1
            if dist[t] == INF:
                return -1

            d = f
            v = t
            while v != s:
                d = min(d, G[prevv[v]][preve[v]][1])
                v = prevv[v]
            f -= d
            res += d * dist[t]
            v = t
            while v != s:
                e = G[prevv[v]][preve[v]]
                e[1] -= d
                G[v][e[3]][1] += d
                v = prevv[v]
        return res


n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
graph = MinCostFlow(n + 2)
for i in range(n):
    graph.addEdge(n, i, 1, 1)
for i in range(n):
    if sum(g[i]) != 0:
        graph.addEdge(i, n+1, 1, 1)
    for j in range(n):
        if g[i][j] == 0:
            continue
        graph.addEdge(i, j, 1, 0)
print(graph.minCostFlow(n, n+1, 2))
