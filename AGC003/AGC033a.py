from collections import deque
import sys
input = sys.stdin.readline

h, w = map(int, input().split())
a = [[j == '#' for j in input()] for _ in range(h)]

queue = deque([(i, j, 0) for i in range(h)
               for j in range(w) if a[i][j]])

ans = 0

d = ((1, 0), (0, 1), (0, -1), (-1, 0))


# def bfs(y, x, cnt):

# if (y < 0 or h <= y or x < 0 or w <= x or not a[y][x]):
#    return
#print(y, x, cnt)

# print(queue)
while (queue):
    y, x, cnt = queue.popleft()
    # print(l)
    #print(ans, cnt)
    #ans = max(ans, cnt)
    for ddx, ddy in d:
        #print(ddx, ddy)
        if (0 <= y+ddy < h and 0 <= x+ddx < w and not a[y+ddy][x+ddx]):
            a[y+ddy][x+ddx] = True
            queue.append((y + ddy, x+ddx, cnt+1))
    # print(queue)
    #print(a, sep='\n')
print(ans)
