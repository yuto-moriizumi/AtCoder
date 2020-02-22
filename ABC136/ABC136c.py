# ABC136c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
h = list(map(int, input().split()))

mak = h[0]
for i in h:
    if (mak > i):
        if (mak - i > 1):
            print("No")
            exit()
    else:
        mak = i
print("Yes")
