d, n = map(int, input().split())
ans = 100**d*n
if ans % 100**(d+1) == 0:
    ans += 100**d
print(ans)
