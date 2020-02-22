# ABC007c
import sys
import collections
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
maze = [list(input()) for _ in range(r)]
ans = [[1000000] * c for _ in range(r)]

queue = collections.deque()


def bfs(y, x, cnt):
    if (y < 0 or r <= y or x < 0 or c <= x):
        return
    if (maze[y][x] == '#'):
        return
    ans[y][x] = cnt
    maze[y][x] = '#'
    queue.append([y + 1, x, cnt + 1])
    queue.append([y - 1, x, cnt + 1])
    queue.append([y, x+1, cnt + 1])
    queue.append([y, x-1, cnt+1])
    return


queue.append([sy-1, sx-1, 0])

while (len(queue) > 0):

    l = queue.popleft()
    # print(l)
    bfs(l[0], l[1], l[2])

print(ans[gy-1][gx-1])
