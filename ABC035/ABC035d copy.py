# ABC035d
def main():
    import sys
    import collections
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    n, m, t = map(int, input().split())
    A = list(map(int, input().split()))
    INF = 10**12

    class Edge:  # 通常の辺
        def __init__(self, to, cost):
            self.to = to
            self.cost = cost

    class Dijkstra:  # ダイクストラ法
        def __init__(self, n):
            self.n = n
            self.dist = [INF for i in range(n)]
            self.edges = [list() for _ in range(n)]
            self.q = collections.deque()

        def calcShortest(self, start):
            self.q.append((start, 0))
            while(len(self.q) != 0):
                v, cost = self.q.popleft()
                if self.dist[v] < cost:
                    continue
                self.dist[v] = cost
                for edge in self.edges:
                    self.q.append((edge.to, cost+edge.cost))

        def addEdge(self, st, gl, cost):
            self.edges[st] = (Edge(gl, cost))

    prograde = Dijkstra(n)
    retrograde = Dijkstra(n)

    for _ in range(m):
        a, b, c = map(int, input().split())
        prograde.addEdge(a-1, b-1, c)
        retrograde.addEdge(b-1, a-1, c)

    prograde.calcShortest(0)
    retrograde.calcShortest(0)

    ans = t*A[0]
    for i in range(n):
        ans = max(ans, (t-prograde.dist[i]-retrograde.dist[i])*A[i])
    print(ans)


if __name__ == '__main__':
    main()
