# ABC111c
from collections import Counter
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def calc():
    ans = 0
    for i in range(len(v)):
        if i % 2 == 0:
            if v[i] != f:
                ans += 1
        else:
            if v[i] != f2:
                ans += 1
    return ans


n = int(input())
v = list(map(int, input().split()))
V1 = Counter(v[::2]).most_common()
V2 = Counter(v[1::2]).most_common()
f = V1[0][0]
f2 = V2[0][0]
if f == f2:
    if len(V2) > 1:
        f2 = V2[1][0]
    else:
        f2 = 'x'
    a = calc()
    if len(V1) > 1:
        f = V1[1][0]
    else:
        f = 'x'
    f2 = V2[0][0]
    print(min(a, calc()))
else:
    print(calc())
