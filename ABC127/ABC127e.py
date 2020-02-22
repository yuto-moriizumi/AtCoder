import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())


a = [(1, 1), (2, 1), (2, 2)]


def kyori(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])


cost = 0
for i in range(1, k):
    for j in range(i + 1, k+1):
        cost += kyori(a[i-1], a[j-1])

print(cost)
