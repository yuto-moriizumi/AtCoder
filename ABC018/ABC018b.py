# ABC018b
import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

s = list(input()[:-1])
n = int(input())
for _ in range(n):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    for i in range(l, math.ceil((l+r)/2)):
        t = s[i]
        s[i] = s[r-(i-l)]
        s[r-(i-l)] = t
print(*s, sep='')
