# ABC125a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a, b, t = map(int, input().split())
now = 0
bis = 0
while(now <= t):
    now += a
    bis += b
print(bis-b)
