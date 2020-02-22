# ABC028a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
if n == 100:
    print('Perfect')
elif n >= 90:
    print('Great')
elif n >= 60:
    print('Good')
else:
    print('Bad')
