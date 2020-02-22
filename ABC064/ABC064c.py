# ABC064c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))
ans = 0
color = [False]*8
for i in a:
    if i >= 3200:
        ans += 1
        continue
    color[i//400] = True
print(max(color.count(True), 1), ans+color.count(True))
