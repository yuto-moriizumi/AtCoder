# ABC106b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

ans = 0

for i in range(1, n + 1, 2):
    cnt = 2
    for j in range(2, i):
        if (i % j == 0):
            cnt += 1
    if (cnt == 8):
        ans += 1
    #print(i, cnt)
print(ans)
