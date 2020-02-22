# 最初に入れておくとinputが早くなる
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

sSet = {}
tSet = {}


def sSelect(i, l):
    if (i >= n):
        if (sSet.get(tuple(l)) == None):
            sSet[tuple(l)] = 1
            return
        sSet[tuple(l)] += 1
        return
    sSelect(i + 1, l)
    l.append(s[i])
    sSelect(i + 1, l)
    return


sSelect(0, [])

print(sSet)
