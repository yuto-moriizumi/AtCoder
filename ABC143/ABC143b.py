# ABC143b
import itertools
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
d = list(map(int, input().split()))

ans = 0

for i, j in itertools.combinations(d, 2):
    ans += i * j

print(ans)
