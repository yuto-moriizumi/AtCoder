import math
import collections

n = int(input())
num = [int(input()) for _ in range(n)]
num.sort()
num2 = collections.deque(num)

center = math.ceil(n / 2) - 1
ans = 0
last = num[center]
cnt = 1
if (abs(num2[-1] - last) > abs(num2[0] - last)):
    LR = 1
else:
    LR = 0

while (True):
    if (cnt == n):
        break
    if (LR == 0):
        t = num2.popleft()
    else:
        t = num2.pop()
    cnt += 1
    LR = 1 - LR
    ans += abs(last - t)
    last = t

curans = ans

num2 = collections.deque(num)

center = math.ceil(n / 2)
ans = 0
last = num[center]
cnt = 1
if (abs(num2[-1] - last) > abs(num2[0] - last)):
    LR = 1
else:
    LR = 0

while (True):
    if (cnt == n):
        break
    if (LR == 0):
        t = num2.popleft()
    else:
        t = num2.pop()
    cnt += 1
    LR = 1 - LR
    ans += abs(last - t)
    last = t

print(max(ans, curans))
