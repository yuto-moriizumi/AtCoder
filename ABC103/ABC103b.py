# ABC103b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

s = input()[:-1]
t = input()[:-1]

tt = t

for _ in range(len(t)):
    tt = tt[1:]+tt[0]
    if (s == tt):
        print('Yes')
        exit()
print('No')

