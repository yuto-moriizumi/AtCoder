# ABC137c
import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
s = dict()
for _ in range(n):
    t = tuple(sorted(input()))
    if (s.get(t) == None):
        s[t] = 1
    else:
        s[t] += 1
c = 0
for i in s.values():
    if(i>1):
        c += math.factorial(i) // (math.factorial(i - 2) * math.factorial(2))
print(c)
