# ABC072b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

s = input()
ans = ''

for i in range(0, len(s), 2):
    ans += s[i]
print(ans)
