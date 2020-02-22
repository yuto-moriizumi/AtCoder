from collections import Counter
s = input()
l = len(s)

ma = 0
mi = 10 * 10


c = Counter(s)
for i in c.most_common():
    ma = max(ma, i[1])
    mi = min(mi, i[1])
if len(c) == 1 and l == 1:
    print('YES')
    exit(0)
if len(c) == 2 and l == 2:
    print('YES')
    exit(0)
if len(c) == 3 and ma-mi <= 1:
    print('YES')
    exit(0)
print('NO')
