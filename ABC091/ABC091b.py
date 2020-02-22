# ABC091b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
s = dict()
for _ in range(n):
    i = input()[:-1]
    if (s.get(i) == None):
        s[i] = 1
    else:
        s[i] += 1
m = int(input())
for _ in range(m):
    i = input()[:-1]
    if (s.get(i) == None):
        s[i] = -1
    else:
        s[i] -= 1
print(max(max(s.values()), 0))
