# ABC135c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = 0

for i in range(n):
    if (a[i] < b[i]):
        taosu = min(a[i + 1], b[i] - a[i])
        a[i + 1] -= taosu
        c += taosu+a[i]
        a[i] = 0
    else:
        c += b[i]
        a[i] -= b[i]
print(c)
