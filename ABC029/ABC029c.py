# ABC029c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
ans = []


def create(i, s):
    if i == n:
        ans.append(s)
        return
    create(i+1, s+'a')
    create(i+1, s+'b')
    create(i+1, s+'c')


create(0, '')
print(*sorted(ans), sep='\n')
