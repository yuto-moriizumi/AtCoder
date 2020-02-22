# ABC079a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = list(input()[:-1])
print('YNeos'[n[1] != n[2] or n.count(n[1]) < 3::2])
