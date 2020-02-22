# ABC110b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

if (max(max(x), X) < min(min(y), Y)):
    print('No War')
    exit()
print('War')
