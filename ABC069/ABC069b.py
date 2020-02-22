# ABC069b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

s = input()[:-1]

print(s[0]+str(len(s)-2)+s[-1])
