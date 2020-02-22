#ABC048b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a, b, x = map(int, input().split())

ans = b // x - a // x
if (a % x == 0):
    ans += 1
print(ans)