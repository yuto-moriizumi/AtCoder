from collections import deque
import sys
input = sys.stdin.readline

# スタック最大数をセット
sys.setrecursionlimit(10**6)
h, w, n = map(int, input().split())
maze = []
sx = 0
sy = 0
for j in range(h):
    i = input()[:-1]
    idx = i.find('S')
    if (idx != -1):
        sx = idx
        sy = j
    maze.append(list(i))
queue = deque()
target = 1

visited = [[False]*w for _ in range(h)]

queue.append((sy, sx, 0))
d = ((1, 0), (-1, 0), (0, 1), (0, -1))
while (queue):
    y, x, cnt = queue.popleft()
    if (x < 0 or w <= x or y < 0 or h <= y or maze[y][x] == 'X'):
        continue
    if (visited[y][x]):
        continue
    #print(y, x, cnt)
    if (maze[y][x] == str(target)):
        #print('find', y, x, target)
        if (target == n):
            print(cnt)
            exit()
        visited = [[False]*w for _ in range(h)]
        queue.clear()
        queue.append((y, x, cnt))
        target += 1
        # for i in maze:
        # print(i)
    visited[y][x] = True
    for dy, dx in d:
        queue.append((y+dy, x+dx, cnt+1))
