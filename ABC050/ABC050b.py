# ABC050b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
t = list(map(int, input().split()))
m = int(input())
p = [list(map(int, input().split())) for _ in range(m)]

for i in range(m):
    print(sum(t)-t[p[i][0]-1]+p[i][1])
