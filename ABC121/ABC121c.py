import sys
from operator import itemgetter
input = sys.stdin.readline

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
AB.sort(key=itemgetter(0))

count = 0
index = 0
for i in range(N):
    count += AB[i][1]
    if(count >= M):
        count -= AB[i][1]
        index = i
        break

money = 0
for i in range(index):
    money += AB[i][0]*AB[i][1]
money += (M-count)*AB[index][0]
print(money)
