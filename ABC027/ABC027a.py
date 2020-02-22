# ABC027a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

l = list(map(int, input().split()))
l.sort()
print(l[0] if l.count(l[0]) == 1 else l[2])
