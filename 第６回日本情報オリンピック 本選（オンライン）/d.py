n = int(input())
m = int(input())
e = [set() for _ in range(n)]
visited = [False]*n
for _ in range(m):
    a, b = map(int, input().split())
    e[b-1].add(a-1)

ans = []


def visit(i):
    if visited[i]:
        return
    visited[i] = True
    for v in e[i]:
        visit(v)
    ans.append(i)


for i in range(n):
    visit(i)

flag = 0
for i in range(n-1):
    print(ans[i]+1)
    if (not ans[i+1] in e[ans[i]])and(not ans[i] in e[ans[i+1]]):
        flag = 1
print(ans[-1]+1)
print(flag)
