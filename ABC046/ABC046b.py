#ABC046b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
print(k * (k - 1)**(n - 1))
