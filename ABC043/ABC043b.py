#ABC043b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

s = input()
ans = ""
for i in s:
    if (i == "B"):
        ans = ans[:len(ans) - 1]
    else:
        ans += i

print(ans)