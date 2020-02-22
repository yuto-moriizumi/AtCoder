def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    n = int(input())
    edge = [dict() for _ in range(n)]
    dist = [0]*n
    for _ in range(n-1):
        u, v, w = map(int, input().split())
        edge[u-1].update({v-1: w})
        edge[v-1].update({u-1: w})

    def dfs(i, pre, d):
        dist[i] = d
        for v in edge[i].keys():
            if v == pre:
                continue
            dfs(v, i, d+edge[i][v])

    dfs(0, -1, 0)
    # print(dist)

    for i in dist:
        if i % 2 == 0:
            print(0)
        else:
            print(1)


if __name__ == '__main__':
    main()
