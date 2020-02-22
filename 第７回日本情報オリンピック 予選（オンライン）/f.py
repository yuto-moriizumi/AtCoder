def main():
    import sys
    import collections
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # map(int, input().split())

    n, k = map(int, input().split())
    dist = [[10**7]*n for i in range(n)]

    class Edge:
        def __init__(self, to, yen):
            self.to = to
            self.yen = yen

    edges = [list() for _ in range(n)]
    q = collections.deque()

    def update(s):
        while(len(q) != 0):
            v, cost = q.popleft()
            if dist[s][v] < cost:
                continue
            dist[s][v] = cost
            for i in edges[v]:
                q.append((i.to, cost+i.yen))

    for _ in range(k):
        a, *b = map(int, input().split())
        if a == 1:
            edges[b[0]-1].append(Edge(b[1]-1, b[2]))
            edges[b[1]-1].append(Edge(b[0]-1, b[2]))
        else:
            q.append((b[0]-1, 0))
            update(b[0]-1)
            ans = dist[b[0]-1][b[1]-1]
            if ans == 10**7:
                print(-1)
            else:
                print(ans)
        #print(a, b)

    # print(dist)


if __name__ == '__main__':
    main()
