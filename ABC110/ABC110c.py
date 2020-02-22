# ABC110c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

s = input()[:-1]
t = input()[:-1]

alphabet = ['abcdefghijklmnopqrstuvwxyz'].split()

for i in range(len(s)):
    if s[i] != t[i]:
        #print(i, s, s[i], t[i])
        s = s.replace(s[i], t[i])
        # print(s)
print(s)
print(t)
