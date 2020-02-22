# ABC139a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

s = input()
t = input()

count = 0
for i in range(3):
    if (s[i] == t[i]):
        count += 1

print(count)
