# ABC076c
import sys
import re
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

ss = input()[:-1].replace('?', '.')
t = input()[:-1]

ans = []
for i in range(len(ss) - len(t) + 1):
    m = re.match(ss[i:i+len(t)], t)
    if (m != None):
        ans.append(ss[:i] + t + ss[i + len(t):])
if (len(ans) == 0):
    print('UNRESTORABLE')
    exit()
for i in range(len(ans)):
    ans[i] = ans[i].replace('.', 'a')
ans.sort()
print(ans[0])
