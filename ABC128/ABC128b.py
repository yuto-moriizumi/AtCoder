from operator import itemgetter
import sys
input = sys.stdin.readline

n = int(input())
s = []
for i in range(n):
    ts, tp = input().split()
    s.append([ts, int(tp), i+1])
s.sort(key=itemgetter(1), reverse=True)
s.sort(key=itemgetter(0))
for i in s:
    print(i[2])
