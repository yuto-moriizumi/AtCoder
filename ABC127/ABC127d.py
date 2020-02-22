from operator import itemgetter
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = []
for _ in range(m):
    tb, tc = map(int, input().split())
    b.append([tb, tc])
a.sort()
b.sort(key=itemgetter(1), reverse=True)

c = 0
flag = False
for j in range(m):
    if (flag):
        break
    for i in range(b[j][0]):
        if (c >= len(a) or a[c] >= b[j][1]):
            flag = True
            break
        a[c] = b[j][1]
        c += 1

print(sum(a))
