# ABC010c
import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

tax, tay, tbx, tby, t, v = map(int, input().split())
n = int(input())
girls = [tuple(map(int, input().split())) for _ in range(n)]


def euclidean_distance(pos1, pos2):
    t = 0
    for i in range(len(pos1)):
        t += (pos1[i] - pos2[i]) ** 2
    return math.sqrt(t)


for girl in girls:
    if euclidean_distance((tax, tay), girl) + euclidean_distance((tbx, tby), girl) <= t * v:
        print('YES')
        exit(0)
print('NO')
