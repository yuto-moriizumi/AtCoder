# ABC114b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

s = input()
ans = 99999999

for i in range(len(s)-3):
    ans = min(ans, abs(753-int(s[i:i+3])))
print(ans)
