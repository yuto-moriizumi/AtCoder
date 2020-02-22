import bisect
d = int(input())
n = int(input())
m = int(input())
ds = [int(input()) for _ in range(n-1)]
ks = [int(input()) for _ in range(m)]
ds.append(0)
ds.append(d)
ds.sort()
ks.sort()

ans = 0
for i in ks:
    left = bisect.bisect_left(ds, i)
    #print(i, left-1, i - ds[left-1])
    if ds[left] == i:
        continue
    leftDist = i - ds[left-1]
    right = bisect.bisect_right(ds, i)
    #print(i, right, abs(ds[right]-i))
    rightDist = abs(ds[right]-i)
    ans += min(leftDist, rightDist)
print(ans)
