# ABC041c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    a[i] = (a[i], i)

for i in sorted(a, reverse=True):
    print(i[1]+1)
