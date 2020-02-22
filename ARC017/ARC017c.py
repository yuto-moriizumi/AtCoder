import bisect
n, x = map(int, input().split())
w = [int(input()) for _ in range(n)]
w1 = w[:n//2]
w2 = w[n // 2:]
w1w = list()
w2w = list()


def dfs1(i, weight):
    if i == n // 2:
        w1w.append(weight)
        return
    dfs1(i + 1, weight + w1[i])
    dfs1(i + 1, weight)


dfs1(0, 0)
# print(w1w)


def dfs2(i, weight):
    if i == len(w2):
        w2w.append(weight)
        return
    dfs2(i + 1, weight + w2[i])
    dfs2(i+1, weight)


dfs2(0, 0)
w2w.sort()
ans = 0
# print(w2w)
for i in w1w:
    pos = bisect.bisect_left(w2w, x - i)
    posR = bisect.bisect_right(w2w, x - i)
    #print(i, pos, w2w[pos], posR)
    ans += posR-pos
print(ans)
