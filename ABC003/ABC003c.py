# ABC003c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
r = list(map(int, input().split()))
r.sort()
c = 0
for i in r[-min(k, len(r)):]:
    c = (c+i)/2
print(c)
