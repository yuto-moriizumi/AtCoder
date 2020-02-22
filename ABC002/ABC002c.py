# ABC002c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

Ax, Ay, Bx, By, Cx, Cy = map(int, input().split())
print(abs((Cy-Ay)*(Bx-Ax)-(Cx-Ax)*(By-Ay))/2)
