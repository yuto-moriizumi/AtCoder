# ABC118b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
a = [list(map(int, input().split()))[1:] for _ in range(n)]
ans = set(a[0])
for i in a:
    ans = ans.intersection(set(i))
print(len(ans))
