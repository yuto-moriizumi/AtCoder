# ABC033a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = input()[:-1]
print('SAME' if n.count(n[0]) == 4 else 'DIFFERENT')
