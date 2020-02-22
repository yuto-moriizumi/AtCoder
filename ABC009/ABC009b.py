# ABC009b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
food = [int(input()) for _ in range(n)]
food = set(food)
food = sorted(list(food), reverse=True)
print(food[1])
