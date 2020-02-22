# 最初に入れておくとinputが早くなる
from operator import itemgetter
import sys
input = sys.stdin.readline

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
l.sort(key=itemgetter(1))

sate = [0]
flag = True

for i in range(n):
    sate.append(sate[i] + l[i][0])
    if (sate[i + 1] > l[i][1]):
        flag = False
        print("No")
        exit()
print("Yes")
