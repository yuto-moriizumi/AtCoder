# ABC140b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

manzoku = 0

manzoku += b[a[0] - 1]

#print('eat:' + str(a[0]))
# print(manzoku)
for i in range(1, n):
    #print('eat:' + str(a[i]))
    manzoku += b[a[i]-1]
    if a[i] - a[i - 1] == 1:
        # print('hi:'+str(c[a[i-1]-1]))
        manzoku += c[a[i-1]-1]
    # print(manzoku)

print(manzoku)
