# ABC058b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

o = input()
e = input()

for i in range(len(o) + len(e)):
    if (i % 2 == 1):
        print(e[i // 2], end='')
    else:
        print(o[i//2], end='')
