# ABC101b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = input()[:-1]
print('Yes' if int(n) % sum(list(map(int, list(n)))) == 0 else 'No')
