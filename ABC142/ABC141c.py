# ABC141c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))

t = []

for i in range(n):
    t.append([a[i], i])
t.sort()

for i in t:
    print(i[1]+1, end=' ')
