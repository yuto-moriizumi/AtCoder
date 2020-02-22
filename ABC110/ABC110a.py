# ABC110a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = list(map(int, input().split()))
n.sort(reverse=True)
print(n[0]*10+n[1]+n[2])
