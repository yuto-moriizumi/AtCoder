# ABC034a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

x, y = map(int, input().split())
print('Better' if y > x else 'Worse')
