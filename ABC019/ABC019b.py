# ABC019b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

s = input()[:-1]

mode = s[0]
count = 0
ans = ''
for i in s:
    if i == mode:
        count += 1
        continue
    ans += mode+str(count)
    mode = i
    count = 1
ans += mode+str(count)
print(ans)
