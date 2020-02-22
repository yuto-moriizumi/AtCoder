# ABC141a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
odd = 0
even = 0
for i in range(1, n + 1):
    if (i % 2 == 0):
        even += 1
    else:
        odd += 1
print(odd/(odd+even))
