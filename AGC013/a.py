n = int(input())
a = list(map(int, input().split()))

mode = 0
ans = 0
for i in range(1, n):
    if a[i]-a[i-1] == 0:
        continue
    if a[i]-a[i-1] > 0:
        if mode == 0:
            mode = 1
        if mode == -1:
            ans += 1
            mode = 0
    if a[i]-a[i-1] < 0:
        if mode == 0:
            mode = -1
        if mode == 1:
            ans += 1
            mode = 0
print(ans+1)
