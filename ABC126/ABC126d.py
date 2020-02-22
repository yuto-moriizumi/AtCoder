import sys
input = sys.stdin.readline

n = int(input())
point = [[0, 0, 0], [1, 0, 0]]

for i in range(2, n+1):
    point.append([i, 0, 3])

for _ in range(n-1):
    u, v, w = map(int, input().split())
    point[v][0] = u
    point[v][1] = w

for i in range(1, n + 1):
    if (point[i][0] != i):
        if (point[i][1] % 2 == 0):
            point[i][2] = point[point[i][0]][2]
        else:
            point[i][2] = 1 - point[point[i][0]][2]
    else:
        point[i][2] = 0

for i in range(1, n+1):
    #print(i, point[i])
    print(point[i][2])
