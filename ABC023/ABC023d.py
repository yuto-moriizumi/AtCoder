# ABC023d
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
fusen = []
maxH = 0
maxS = 0
for _ in range(n):
    h, s = map(int, input().split())
    fusen.append([h, s])
    maxH = max(maxH, h)
    maxS = max(maxS, s)


def evaluate(n):
    seigen = []
    for i in fusen:
        if n - i[0] < 0:
            return 1
        seigen.append((n-i[0])//i[1])
    seigen.sort()
    for i in range(len(fusen)):
        if seigen[i] < i:
            return 1
    return -1


def binary_search(low, high):
    lowest = low
    highest = high
    while low <= high:
        mid = (low + high) // 2
        guess = evaluate(mid)
        if guess == 0:
            return [mid, mid]
        if guess < 0:
            high = mid - 1
            highest = mid
        else:
            low = mid + 1
            lowest = mid

    return [lowest, highest]


print(binary_search(maxH, maxH+maxS*n)[1])
