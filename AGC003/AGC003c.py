n = int(input())
a = [int(input()) for _ in range(n)]

ki = set()

for i in range(0, n, 2):
    ki.add(a[i])
# print(ki)
ans = 0
a.sort()
for i in range(1, n, 2):
    if a[i] in ki:
        ans += 1
print(ans)
