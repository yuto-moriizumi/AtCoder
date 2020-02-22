# ABC077c
from bisect import bisect_left
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort()
b.sort()
c.sort()

ans = 0
for i in b:
    smallPos = bisect_left(a, i)
    BigPos = bisect_left(c, i+1)
    ans += smallPos*(n-BigPos)
print(ans)
