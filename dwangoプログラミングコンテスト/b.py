s = input()
ld = dict()
cc = 0
i = 0
while i < len(s) - 1:
    if s[i: i + 2] == '25':
        cc += 1
        i += 2
        continue
    if cc == 0:
        i += 1
        continue
    if ld.get(cc) == None:
        ld[cc] = 0
    ld[cc] += 1
    cc = 0
    i += 1
if cc != 0:
    if ld.get(cc) == None:
        ld[cc] = 0
    ld[cc] += 1
    cc = 0
    i += 1
# print(ld)

ans = 0
for k in ld:
    ans += (k+1)*k//2*ld[k]
    #print(k, ld[k])
print(ans)
