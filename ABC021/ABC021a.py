# ABC021a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
b = bin(n)[2:]
c = 1
ans = []
while(len(b) > 0):
    if int(b[-1]) != 0:
        ans.append(c*int(b[-1]))
    b = b[:-1]
    c *= 2

print(len(ans))
for i in ans:
    print(i)
