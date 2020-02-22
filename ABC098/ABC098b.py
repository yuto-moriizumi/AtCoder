# ABC098b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
s = input()

ans = 0
for i in range(1, n):
    ans = max(ans, len(set(s[:i]).intersection(set(s[i:]))))
print(ans)
