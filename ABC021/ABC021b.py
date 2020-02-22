# ABC021b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
a, b = map(int, input().split())
k = int(input())
p = list(map(int, input().split()))
if len(set(p)) == len(p) and not a in p and not b in p:
    print('YES')
    exit(0)
print('NO')
