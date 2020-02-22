# ABC061d
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


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


n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, -c))
ans = BellmanFord(edges, n, 1)
print(-ans[n-1] if ans != -1 else 'inf')
