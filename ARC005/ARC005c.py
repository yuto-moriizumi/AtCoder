# 最初に入れておくとinputが早くなる
from collections import deque
import sys
input = sys.stdin.readline

# スタック最大数をセット
sys.setrecursionlimit(10**6)
h, w = map(int, input().split())
c = []
sy = 0
sx = 0
gx = 0
gy = 0
for j in range(h):
    i = input()[:-1]
    c.append(list(i))
    ind = i.find('s')
    if (ind != -1):
        sx = ind
        sy = j
    else:
        ind = i.find('g')
        if (ind != -1):
            gx = ind
            gy = j

queue = deque()

queue.append((sy, sx, 0))

table = [[99999]*w for _ in range(h)]

d = ((0, 1), (0, -1), (1, 0), (-1, 0))
while (queue):
    y, x, cnt = queue.popleft()
    # print(y, x, cnt)
    if (y < 0 or h <= y or x < 0 or w <= x):
        continue
    if (c[y][x] == 'g'):
        print('YES')
        exit()
    if (c[y][x] == '#'):
        cnt += 1
        if (cnt > 2):
            continue
        if (table[y][x] <= cnt):
            continue
        table[y][x] = cnt
        for dy, dx in d:
            queue.append((y + dy, x + dx, cnt))
        continue
    if (cnt > 2):
        continue
    if (table[y][x] <= cnt):
        continue
    table[y][x] = cnt
    for dy, dx in d:  # 壁ではないマスだったら周囲を優先的に探索する
        queue.appendleft((y + dy, x + dx, cnt))
# for i in table:
#    print(i)
print('NO')
