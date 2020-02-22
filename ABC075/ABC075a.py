# ABC075a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a = sorted(list(map(int, input().split())))
print(a[0] if a.count(a[0]) != 2 else a[2])
