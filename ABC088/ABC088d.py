import collections
h, w = map(int, input().split())
queue = collections.deque()
maze = [list(input()) for _ in range(h)]

origin = 0
for i in maze:
    origin += i.count('#')
# print(origin)


def bfs(y, x, cnt):
    if (y < 0 or h <= y or x < 0 or w <= x):
        return
    if (maze[y][x] != '.'):
        return
    maze[y][x] = cnt
    if (y == h - 1 and x == w - 1):
        return cnt
    queue.append([y + 1, x, cnt + 1])
    queue.append([y - 1, x, cnt + 1])
    queue.append([y, x+1, cnt+1])
    queue.append([y, x-1, cnt+1])


queue.append([0, 0, 0])
while (len(queue) > 0):
    l = queue.popleft()
    bfs(l[0], l[1], l[2])
if (maze[h - 1][w - 1] == '.'):
    print(-1)
    exit()

# print(ans)
print(h*w-origin-maze[h-1][w-1]-1)
