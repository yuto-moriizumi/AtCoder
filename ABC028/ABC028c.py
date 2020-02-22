# ABC028c
import sys
import itertools
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a = list(map(int, input().split()))
ans = set()

for i in itertools.combinations(a, 3):
    ans.add(sum(i))
ans = sorted(list(ans), reverse=True)

print(ans[2])
