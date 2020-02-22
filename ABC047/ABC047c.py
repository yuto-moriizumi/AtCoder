# ABC047c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

s = input()[:-1]
mode = s[0]
ans = 0
for i in s:
    if i != mode:
        mode = i
        ans += 1
print(ans)
