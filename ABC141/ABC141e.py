# ABC141e
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
s = input()[:-1]

setsu = []
for i in range(n):
    setsu.append(s[i:])
# print(setsu)
setsu.sort()
print(setsu)

fm = []

for i in range(n - 1):
    s = setsu[i] if len(setsu[i]) < len(setsu[i+1]) else setsu[i+1]
    for j in range(len(s)):
        s[]
    l = 0
    if (len(setsu[i]) > len(setsu[i + 1])):
        l = setsu[i].count(setsu[i + 1])
    else:
        l = setsu[i+1].count(setsu[i])
    fm.append([min(len(setsu[i]), len(setsu[i + 1])), l, i])
print(fm)

fm.sort(reverse=True)

print(fm)
ind = -1
for i in range(len(fm)):
    if (fm[i][1] > 1):
        ind = i
        break
print(ind)

# print(setsu[fm[ind][2]])

print(len(setsu[fm[ind][2]]) if ind != -1 else 0)

