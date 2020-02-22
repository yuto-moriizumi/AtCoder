# ABC146d
ans = 1


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    # map(int,input().split())

    n = int(input())

    edges = [list() for _ in range(n)]
    colors = [-1] * (n - 1)

    for i in range(n - 1):
        a, b = map(int, input().split())
        edges[a - 1].append((b - 1, i))
        edges[b - 1].append((a - 1, i))

    def dfs(i, color, pre):
        nc = 0 if color != 0 else 1
        for e in edges[i]:
            if e[0] == pre:
                continue
            global ans
            if ans < len(edges[i]):
                ans = len(edges[i])
            colors[e[1]] = nc
            dfs(e[0], nc, i)
            nc += 1
            if nc == color:
                nc += 1
    dfs(0, -1, -1)
    print(ans)
    for i in colors:
        print(i+1)


if __name__ == '__main__':
    main()
