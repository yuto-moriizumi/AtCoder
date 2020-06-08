# ABC004c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

card = [i for i in range(1, 7)]
for i in range(n % 30):
    t = card[i % 5]
    card[i % 5] = card[i % 5+1]
    card[i % 5+1] = t
print(*card, sep='')
