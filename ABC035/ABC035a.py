# ABC035a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

w, h = map(int, input().split())

print('4:3' if w/h == 4/3 else '16:9')
