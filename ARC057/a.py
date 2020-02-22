a, k = map(int, input().split())
if k == 0:
    print(10**12*2-a)
    exit(0)
ans = 0
while(a < 10**12*2):
    a += a*k+1
    ans += 1
print(ans)
