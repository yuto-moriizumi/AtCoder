# ABC080b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = input()[:-1]
num = int(n)
if (num % sum(list(map(int, list(n)))) == 0):
    print('Yes')
else:
    print('No')
