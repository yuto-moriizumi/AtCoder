# ABC073b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in l:
    ans += i[1]-i[0]+1
print(ans)
