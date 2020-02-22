# ABC134e
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
a = []
b = 10**9

for _ in range(n):
    a.append(int(input()))

c = 0
for i in range(n):
    if (a[i] <= b):
        c += 1
        b = a[i]
print(c)
