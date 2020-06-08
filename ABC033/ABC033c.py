# ABC033c
import sys
sys.setrecursionlimit(10**6)

s = input()
kou = list(map(eval, s.split('+')))
print(len(kou)-kou.count(0))
