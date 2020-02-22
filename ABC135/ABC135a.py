# ABC135a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a, b = map(int, input().split())
#print((a + b) / 2)
ans = (a + b) / 2
if (ans.is_integer()):
    print((a + b) // 2)
    exit()
print("IMPOSSIBLE")
