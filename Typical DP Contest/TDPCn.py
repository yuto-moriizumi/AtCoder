import math

n = int(input())
e = [set() for _ in range(n)]
MOD = 10**9+7

for _ in range(n-1):
    a, b = map(int, input().split())
    e[a-1].add(b-1)
    e[b-1].add(a-1)


def dfs(i, pre):
    pat = 0
    for v in e[i]:
        if v == pre:
            continue
        pat += dfs(v, i)
    return math.factorial(pat)


ans = 0
for i in range(n):
    for j in e[i]:
        ans += dfs(i, j)*dfs(j, i)
print(ans)
