#ABC044b
import sys
import re
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

w = input()
eimozi = "abcdefghijklmnopqrstuvwxyz"
flag = True
for i in eimozi:
    flag = w.count(i) % 2 == 0
    if (not flag):
        break
print("Yes" if flag else "No")