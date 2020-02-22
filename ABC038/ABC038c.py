# ABC038c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
a = list(map(int, input().split()))
cnt = 0
left = 0
while left < n:
    right = left + 1
    cnt += 1
    while right < n:
        if a[right - 1] < a[right]:
            cnt += 1
            right += 1
            continue

        break
    width = right-left
    cnt += width*(width-1)//2
    left = right
print(cnt)
