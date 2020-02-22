n = int(input())
ondo = [list(map(float, input().split())) for _ in range(n)]
soukei = {'mousyo': 0, 'manatsu': 1, 'natsu': 2,
          'nettai': 3, 'huyu': 4, 'mafuyu': 5}
s = [0]*6
for i, j in ondo:
    if i >= 35:
        s[soukei['mousyo']] += 1
    if 30 <= i < 35:
        s[soukei['manatsu']] += 1
    if 25 <= i < 30:
        s[soukei['natsu']] += 1
    if 25 <= j:
        s[soukei['nettai']] += 1
    if j < 0 and 0 <= i:
        s[soukei['huyu']] += 1
    if i < 0:
        s[soukei['mafuyu']] += 1
print(*s)
