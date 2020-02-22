n, c, k = map(int, input().split())
t = sorted([int(input()) for _ in range(n)])
ans = 1
busNin = 0
busFirstp = 0
for i in range(n):
    if t[i]-t[busFirstp] > k or busNin == c:
        ans += 1
        busNin = 1
        busFirstp = i
        continue
    busNin += 1
print(ans)
