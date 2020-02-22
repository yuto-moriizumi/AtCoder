import re

i = int(input().split()[1])
s = re.sub("AC", "12", input())
k = 0
result = []

print(s)

while k < i:
    ft, et = map(int, input().split())
    result.append(len(re.findall("12", s[ft - 1:et])))
    k += 1

for kekka in result:
    print(kekka)
