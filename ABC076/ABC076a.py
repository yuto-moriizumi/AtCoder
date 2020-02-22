# ABC076a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

r = int(input())
g = int(input())
# (r+ans)/2=g
# r/2+ans/2=g
# ans/2=g-r/2
# ans=2*g-r
print(2*g-r)
