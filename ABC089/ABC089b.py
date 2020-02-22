# ABC089b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
d = {'M': 0, 'A': 0, 'R': 0, 'C': 0, 'H': 0}
for _ in range(n):
    s = input()[:-1]
    if not s[0] in d.keys():
        continue
    d[s[0]] += 1

ans = 0
l = list(d.values())
for i in range(5):
    for j in range(i+1, 5):
        for k in range(j+1, 5):
            ans += l[i]*l[j]*l[k]
print(ans)
