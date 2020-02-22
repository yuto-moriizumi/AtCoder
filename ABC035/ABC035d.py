# ABC035d
def main():
    import sys
    import collections
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    n, m, t = map(int, input().split())
    A = list(map(int, input().split()))

    dist = [[10**12]*n for i in range(2)]

    class Edge:
        def __init__(self, to, cost):
            self.to = to
            self.cost = cost

    edges = [list() for _ in range(n)]
    edgesR = [list() for _ in range(n)]
    q = collections.deque()

    def update(s):
        while(len(q) != 0):
            v, cost = q.popleft()
            if dist[s][v] < cost:
                continue
            dist[s][v] = cost
            for edge in edges[v]:
                q.append((edge.to, cost+edge.cost))

    def update2(s):
        while(len(q) != 0):
            v, cost = q.popleft()
            if dist[s][v] < cost:
                continue
            dist[s][v] = cost
            for edge in edgesR[v]:
                q.append((edge.to, cost+edge.cost))

    for _ in range(m):
        a, b, c = map(int, input().split())
        edges[a-1].append(Edge(b-1, c))
        edgesR[b-1].append(Edge(a-1, c))

    q.append((0, 0))
    update(0)

    q.append((0, 0))
    update2(1)

    ans = t*A[0]
    for i in range(n):
        ans = max(ans, (t-dist[0][i]-dist[1][i])*A[i])
    print(ans)


if __name__ == '__main__':
    main()
