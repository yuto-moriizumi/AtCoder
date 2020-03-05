from itertools import combinations


n = int(input())
s = input()
ans = 0
for i in range(1000):
    num = '{:0=3}'.format(i)
    inds = 0
    indnum = 0
    while inds < len(s) and indnum < 3:
        if s[inds] == num[indnum]:
            indnum += 1
        inds += 1
    if indnum == 3:
        ans += 1
print(ans)
