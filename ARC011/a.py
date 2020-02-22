m, n, N = map(int, input().split())
ans = N
newEnpitsu = N
unUsed = 0
while True:
    oldUnUsed = unUsed
    unUsed = (newEnpitsu+unUsed)-(newEnpitsu+unUsed) // m*m
    newEnpitsu = ((newEnpitsu+oldUnUsed) // m)*n
    ans += newEnpitsu
    if newEnpitsu == 0:
        break
print(ans)
