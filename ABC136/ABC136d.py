# ABC136d
import sys
import re
import math
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

s = input()
l = re.findall("R+L+", s)
ans = []

# print(l)

for i in l:
    R = math.ceil((i.count("R")-1)/2) + math.ceil(i.count("L")/2)
    L = math.ceil(i.count("R")/2) + math.ceil((i.count("L")-1)/2)
    #print(i, R, L)
    for j in range(len(i)):
        if (i[j] == "R" and i[j + 1] == "L"):
            ans.append(L)
            ans.append(R)
            j += 1
        elif(not(i[j] == "L" and i[j - 1] == "R")):
            ans.append(0)
print(*ans)
