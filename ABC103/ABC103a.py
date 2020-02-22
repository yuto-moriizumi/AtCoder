# ABC103a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a = list(map(int, input().split()))
a.sort(reverse=True)
print(abs(a[1]-a[0])+abs(a[1]-a[2]))
