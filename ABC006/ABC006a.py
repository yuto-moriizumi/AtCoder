# ABC006a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
print('YNEOS'[n % 3 != 0::2])
