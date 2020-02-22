# ABC023b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
s = input()[:-1]
tesu = (len(s)-1)//2


def create(st, i):
    if i == tesu+1:
        return st
    if i % 3 == 0:
        return create('b'+st+'b', i+1)
    if i % 3 == 1:
        return create('a'+st+'c', i+1)
    if i % 3 == 2:
        return create('c'+st+'a', i+1)


print(tesu if create('b', 1) == s else -1)
