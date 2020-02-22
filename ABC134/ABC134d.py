# ABC134d
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
a = [-1]
a.extend(list(map(int, input().split())))
ans = [0]*(n+1)


for i in range(n, 0, -1):
    j = 1
    su = 0
    while (i * j <= n):
        su += ans[i * j]
        j += 1
    # print(str(i)+"は"+str(su))
    if (su % 2 == a[i]):
        # print("なので"+str(i)+"を0")
        ans[i] = 0
    else:
        # print("なので"+str(i)+"を1")
        ans[i] = 1

# print(ans)

s = ""
c = 0
for i in range(n+1):
    if (ans[i] == 1):
        c += 1
        s += str(i)+" "
print(c)
if(c != 0):
    print(s)
