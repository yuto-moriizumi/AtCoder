# ABC091c
import sys
from operator import itemgetter
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
red = []
for _ in range(n):
    x, y = map(int, input().split())
    red.append([x, y, x + y])
blue = []
for _ in range(n):
    x, y = map(int, input().split())
    blue.append([x, y, x+y])
red.sort(key=itemgetter(2))
blue.sort(key=itemgetter(2))
rP = 0
bP = 0
ans = 0
used = [False]*n
while (rP < n):
    print(rP)
    for i in range(n):
        if (used[i]):
            continue
        print(red[rP], blue[i])
        if (red[rP][0] < blue[i][0] and red[rP][1] < blue[i][1]):
            print('hi')
            ans += 1
            used[i] = True
            break
    rP += 1

print(ans)
