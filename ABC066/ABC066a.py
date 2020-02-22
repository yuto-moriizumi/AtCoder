# ABC066a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

bell = tuple(map(int, input().split()))
print(sum(bell)-max(bell))
