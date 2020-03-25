# ABC016d
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def intersect(p1, p2, p3, p4):
    tc1 = (p1[0] - p2[0]) * (p3[1] - p1[1]) + (p1[1] - p2[1]) * (p1[0] - p3[0])
    tc2 = (p1[0] - p2[0]) * (p4[1] - p1[1]) + (p1[1] - p2[1]) * (p1[0] - p4[0])
    td1 = (p3[0] - p4[0]) * (p1[1] - p3[1]) + (p3[1] - p4[1]) * (p3[0] - p1[0])
    td2 = (p3[0] - p4[0]) * (p2[1] - p3[1]) + (p3[1] - p4[1]) * (p3[0] - p2[0])
    return tc1 * tc2 < 0 and td1 * td2 < 0


ax, ay, bx, by = map(int, input().split())
a = [ax, ay]
b = [bx, by]
n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]
c = 0

for i in range(1, n + 1):
    p1 = p[i - 1]
    p2 = p[i % n]
    if (intersect(p1, p2, a, b)):
        c += 1
print(c//2+1)
