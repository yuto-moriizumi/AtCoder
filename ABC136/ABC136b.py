# ABC136b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

c = 0
for i in range(1, n+1):
    if (len(str(i)) % 2 == 1):
        c += 1
print(c)
