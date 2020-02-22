# ABC134c
import sys
from operator import itemgetter
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
a = [(i, int(input())) for i in range(n)]

aSort = sorted(a, reverse=True, key=itemgetter(1))

for i in range(n):
    j = 0
    while (aSort[j][0] == i):
        j += 1
    print(aSort[j][1])
