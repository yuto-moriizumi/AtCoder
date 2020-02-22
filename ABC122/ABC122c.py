#import re

i = int(input().split()[1])
s = input()
result = []

for k in range(i):
    ft, et = map(int, input().split())
    result.append(s[ft - 1:et].count("AC"))
    #result.append(len(re.findall("AC", s[ft - 1:et])))

for kekka in result:
    print(kekka)
