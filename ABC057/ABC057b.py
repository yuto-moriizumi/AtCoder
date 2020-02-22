# ABC057b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
c = [list(map(int, input().split())) for _ in range(m)]

ans = [0] * len(a)

for i in range(len(a)):
    for j in range(len(c)):
        if (abs(a[i][0] - c[j][0]) + abs(a[i][1] - c[j][1]) < abs(a[i][0] - c[ans[i]][0]) + abs(a[i][1] - c[ans[i]][1])):
            ans[i] = j

for i in ans:
    print(i+1)
