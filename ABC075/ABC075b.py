# ABC075b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

h, w = map(int, input().split())
s = [input() for _ in range(h)]

ans = [[0] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if (s[i][j] == '#'):
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if (0 <= i+k < h and 0 <= j+l < w and ans[i+k][j+l] != '#'):
                        ans[i+k][j+l] += 1
            ans[i][j] = '#'

for i in ans:
    print(*i, sep='')
