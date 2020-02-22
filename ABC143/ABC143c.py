# ABC143c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
s = input()

ans = []
last = '1'
for i in s:
    if i != last:
        ans.append(i)
        last = i
print(len(ans))
