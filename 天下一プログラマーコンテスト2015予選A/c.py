# Dinic's algorithm O(VE^2)
# 最大独立集合=最大安定集合
# 二部グラフなら頂点数-最大マッチング=最大安定集合
from collections import deque


class Dinic:
    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]

    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)

    def bfs(self, s, t):
        self.level = level = [None]*self.N
        deq = deque([s])
        level[s] = 0
        G = self.G
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in G[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        return level[t] is not None

    def dfs(self, v, t, f):
        if v == t:
            return f
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        INF = 10**9 + 7
        G = self.G
        while self.bfs(s, t):
            *self.it, = map(iter, self.G)
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow


m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]
b = [list(map(int, input().split())) for _ in range(m)]
tree = Dinic(m * n + 2)
diff = 0
for i in range(m):
    for j in range(n):
        if (i + j) % 2 == 0:
            tree.add_edge(i * n + j, m * n, 1)
        else:
            tree.add_edge(m * n + 1, i * n + j, 1)
        if a[i][j] == b[i][j]:
            continue
        diff += 1
        if j + 1 < n and a[i][j] != a[i][j + 1] and a[i][j + 1] != b[i][j + 1] and a[i][j] == b[i][j + 1]:
            if (i + j) % 2 == 0:
                tree.add_edge(i * n + j + 1, i * n + j, 1)
            else:
                tree.add_edge(i * n + j, i * n + j + 1,  1)
        if i + 1 < m and a[i][j] != a[i+1][j]and a[i+1][j] != b[i+1][j] and a[i][j] == b[i+1][j]:
            if (i + j) % 2 == 0:
                tree.add_edge((i + 1) * n + j, i * n + j, 1)
            else:
                tree.add_edge(i * n + j, (i + 1) * n + j,  1)
ans = tree.flow(m * n+1, m * n)
print(diff - ans)
