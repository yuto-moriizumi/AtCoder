#ABC052b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
s = input()
x = 0
maX = 0
for i in s:
    if (i == "I"):
        x += 1
        maX = max(maX, x)
    else:
        x -= 1
print(maX)