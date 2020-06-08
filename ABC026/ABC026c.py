# ABC026c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
b = [[int(input()), i+2] for i in range(n-1)]


def calc(i):
    ma = 0
    mi = 0
    for j in b[i-1:]:
        if j[0] == i:
            t = calc(j[1])
            ma = max(ma, t)
            mi = min(mi, t) if mi != 0 else t
    return 1+ma+mi


print(calc(1))
