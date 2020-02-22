# ABC117c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
sa = []
for i in range(1, m):
    sa.append(x[i]-x[i-1])
print(x)
print(sa)
print('aa')
for haba in range(x[-1]+1):
    last = -99999999
    koma = []

    for i in x:
        if last+haba < i:
            if(len(koma) >= n):
                break
            last = i
            koma.append(i)
    koma.append(x[-1]+1)
    print(koma)
    cost = 0
    for j in range(1, len(koma)):
        for i in range(len(x)):
            if(koma[j-1] == x[i]):
                continue
            if(koma[j-1] <= x[i] < koma[j]):
                print(koma[j-1], x[i], sa[i])
                cost += sa[i]
                continue
            else:
                break
    print(cost)
