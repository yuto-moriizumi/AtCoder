# ABC040b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
ans = 10**15
for w in range(1, n+1):
    height = n // w
    area = w * height
    extra = n-area
    #print(w, height, area)
    ans = min(ans, abs(w-height)+extra)
print(ans)
