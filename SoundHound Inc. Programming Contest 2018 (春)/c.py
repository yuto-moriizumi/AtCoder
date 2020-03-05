# Dinic's algorithm O(VE^2)

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


r, c = map(int, input().split())
tree = Dinic(r*c+2)
C = [input() for _ in range(r)]
vs = 0
for i in range(r):
    for j in range(c):
        if C[i][j] == '*':
            continue
        vs += 1
        if (i + j) % 2 == 0:
            tree.add_edge(r * c, i * c + j,  1)
            if 0 <= i-1 and C[i-1][j] == '.':
                tree.add_edge(i * c + j, (i - 1) * c + j, 1)
            if i+1 < r and C[i+1][j] == '.':
                tree.add_edge(i * c + j, (i + 1) * c + j, 1)
            if 0 <= j-1 and C[i][j-1] == '.':
                tree.add_edge(i * c + j, i * c + j - 1, 1)
            if j+1 < c and C[i][j+1] == '.':
                tree.add_edge(i * c + j, i * c + j + 1, 1)
        else:
            tree.add_edge(i * c + j, r * c+1,  1)
print(vs-tree.flow(r*c, r*c+1))
