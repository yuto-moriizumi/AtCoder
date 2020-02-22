# ABC017b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

s = input()[:-1]
print('YNEOS'[len(s.replace('u', '').replace(
    'k', '').replace('o', '').replace('ch', '')) != 0::2])
