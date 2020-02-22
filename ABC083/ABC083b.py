# ABC083b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, a, b = map(int, input().split())

ans = 0
for i in range(n+1):
    su = sum(list(map(int, list(str(i)))))
    # print(su)
    if (a <= su <= b):
        ans += i
print(ans)
