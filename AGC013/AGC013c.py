n, l, t = map(int, input().split())
ants = [list(map(int, input().split())) for _ in range(n)]

ans = []
for x, w in ants:
    if w == 1:
        ans.append((x + t) % l)
    else:
        ans.append((x-t) % l)

print(ans[-1])
for i in ans[:-1]:
    print(i)
