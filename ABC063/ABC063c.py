# ABC063c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
s = [int(input()) for _ in range(n)]

s.sort()
ans = sum(s)
if ans % 10 != 0:
    print(ans)
    exit(0)
for i in s:
    if i % 10 != 0:
        ans -= i
        print(ans)
        exit(0)
print(0)
