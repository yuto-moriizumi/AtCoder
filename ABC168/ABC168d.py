# ABC168d


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))
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
            self.frm = [-1]*vCount
            self.edges = [list() for _ in range(vCount)]
            self.q = deque()

        def calcShortest(self, start):
            self.q.append((start, 0, -1))
            while(len(self.q) != 0):
                v, cost, frm = self.q.popleft()  # 頂点vへのコストをcostで更新
                if self.dist[v] <= cost:
                    continue
                self.dist[v] = cost
                self.frm[v] = frm
                for edge in self.edges[v]:
                    self.q.append((edge.to, cost+edge.cost, v))

        def addEdge(self, st, gl, cost):
            self.edges[st].append(Edge(gl, cost))

    n, m = map(int, input().split())
    graph = Dijkstra(n)
    for _ in range(m):
        a, b = map(int, input().split())
        graph.addEdge(a - 1, b - 1, 1)
        graph.addEdge(b - 1, a - 1, 1)
    graph.calcShortest(0)
   # print(graph.dist)
    # print(graph.frm)
    if INF in graph.dist:
        print('No')
        exit(0)
    print('Yes')
    for i in graph.frm[1:]:
        print(i+1)


if __name__ == '__main__':
    main()
