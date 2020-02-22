#ABC042b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, l = map(int, input().split())
s = []
for _ in range(n):
    s.append(input().split("\n")[0])
s.sort()

print(*s, sep="")
