unchi = input()
# print(unchi.split('ww'))
ans = 0
for i in unchi.split('ww'):
    if len(i) < 3:
        continue
    if i[0] == 'w':
        i = i[1:]
    if i[-1] == 'w':
        i = i[:-1]
    nW = i.count('w')
    ans += min(nW, (len(i)-nW)//2)
print(ans)
