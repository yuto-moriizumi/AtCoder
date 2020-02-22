#最初に入れておくとinputが早くなる
import sys
input = sys.stdin.readline

n, x = map(int, input().split())
l = list(map(int, input().split()))

for i in range(1,n):
    l[i]=l[i-1]+l[i]

#print(l)
t=0
for _ in l:
    if (l[t] > x):
        break
    t+=1

print(t+1)