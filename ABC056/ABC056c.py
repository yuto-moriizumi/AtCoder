# ABC056c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

x = int(input())


def calc(time, pos):
    if pos == x:
        return time
    if pos > x:
        return -1
    for i in range(time+1, x+1):
        result = calc(i, pos+i)
        if result != -1:
            return result
    return -1


print(calc(0, 0))
