# ABC066b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

s = input()[:-1]


def isGu(st):
    if (len(st) % 2 != 0):
        return False
    flag = True
    for i in range(len(st) // 2):
        if (st[i] != st[i + len(st) // 2]):
            #print(i, i + len(st) // 2)
            flag = False
    return flag


for i in range(2, len(s), 2):
    if (isGu(s[:-i])):
        print(len(s[:-i]))
        exit()
print(0)
