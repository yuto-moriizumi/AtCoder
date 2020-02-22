# ABC039a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a, b, c = map(int, input().split())
print(2*(a*b+b*c+c*a))
