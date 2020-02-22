# ABC056c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

x = int(input())
w = 0
for i in range(1, 10**8):
    if x <= (i+1)*i//2:
        w = i
        break
print(w)
