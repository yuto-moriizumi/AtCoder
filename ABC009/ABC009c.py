# ABC009c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, k = map(int, input().split())
s = list(input()[:-1])


def fm(st):
    tmp = st[0]
    idx = 0
    for i in range(len(st)):
        if (tmp > st[i]):
            tmp = st[i]
            idx = i
    return [tmp, idx]


swap = 0
pos = 0
while (swap < k and pos < len(s)):
    print(swap, pos, s[:pos], s[pos:])
    m = fm(s[pos:])
    if (s[pos] > m[0]):
        t = s[pos]
        s[pos] = m[0]
        s[m[1]+pos] = t
        swap += 2
    pos += 1

print(s)
