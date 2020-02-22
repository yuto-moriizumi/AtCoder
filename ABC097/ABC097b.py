# ABC097b
import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

x = int(input())

ans = 0
for b in range(1, x + 1):
    for p in range(2, math.floor(math.sqrt(x))+2):
        tmp = b ** p
        # print(tmp)
        if (tmp <= x):
            ans = max(ans, tmp)
print(ans)
