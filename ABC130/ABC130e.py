#最初に入れておくとinputが早くなる
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = list(map(int, input().split()))
t= list(map(int, input().split()))

sSet = {}
tSet = {}

for i in range(n):
    for j in range(i+1, n + 1):
        if (sSet.get(tuple(s[i:j])) == None):
            sSet[tuple(s[i:j])] = 1
            continue
        sSet[tuple(s[i:j])] += 1
for i in range(m):
    for j in range(i+1, m + 1):
        if (tSet.get(tuple(t[i:j])) == None):
            tSet[tuple(t[i:j])] = 1
            continue
        tSet[tuple(t[i:j])] += 1

print(sSet)
print(tSet)

count=1

#if (len(sSet) > len(tSet)):
for i in tSet.keys():
    if (sSet.get(i) != None):
        count += tSet[i] * sSet[i]

print(count)