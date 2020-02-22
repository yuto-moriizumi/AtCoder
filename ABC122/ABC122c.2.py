#import re

i = int(input().split()[1])
s = input()
k = 0
f = []
e = []
result = []

for k in range(i):
    ff, ee = map(int, input().split())
    f.append(ff)
    e.append(ee)
    #result.append(s[ft - 1:et].count("AC"))
    #result.append(len(re.findall("AC", s[ft - 1:et])))

for k in range(i):
    print(s[f[k] - 1:e[k]].count("AC"))
