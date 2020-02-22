# ABC063b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

s = input()

dic = dict()

for i in s:
    if (dic.get(i) == None):
        dic[i] = 1
    else:
        print('no')
        exit()
print('yes')
