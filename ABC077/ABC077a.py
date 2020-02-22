# ABC077a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

print('YNEOS'[input()[:-1] != input()[:-1][::-1]::2])
