# ABC015d
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


W = int(input())
N, K = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]

# i番目まででk枚までつかってw幅まででの価値最大


def dfs2(i, k, w):
    if (i < 0 or k < 0 or w < 0):
        return 0
    return max(dfs2(i-1, k-1, w-a[i][0])+a[i][1], dfs2(i-1, k, w))


print(dfs2(N-1, K, W))

# i番目を見ていて、その前までk枚使いw幅つかった


def dfs(i, k, w):
    if (i >= N or k >= K or w >= W):
        return 0
    t = dfs(i + 1, k + 1, w + a[i][0]) + a[i][1]
    n = dfs(i + 1, k, w)
    print(i, k, w, t, n)
    return max(t, n)


#print(dfs(0, 0, 0))
