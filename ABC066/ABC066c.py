# ABC066c
from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


n = int(input())
a = list(map(int, input().split()))
b = deque()
for i in range(n):
    if i % 2 == 0:
        b.append(a[i])
        continue
    b.appendleft(a[i])
if n % 2 == 1:
    b.reverse()
print(*b)
