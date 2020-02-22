# ABC103d
import sys
from operator import itemgetter
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
span = [list(map(int, input().split)) for _ in range(m)]
span.sort(key=itemgetter(1))

setudan = span[0][1]
ans = 1
for i in span:
    if (i[0] >= setudan):
        setudan = i[1]
        ans += 1
print(ans)
