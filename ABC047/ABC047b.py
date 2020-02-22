#ABC047b
import sys
import numpy as np
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

w, h, n = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
square = np.zeros((h, w), dtype="int16")

for i in l:
    if (i[2] == 1):
        square[:, :i[0]] = 1
    elif (i[2] == 2):
        square[:, i[0]:] = 1
    elif (i[2] == 3):
        square[:i[1], :] = 1
    else:
        square[i[1]:, :] = 1
#print(square)
print(w * h - np.sum(square))
