# ABC084b
import sys
import re
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a, b = map(int, input().split())
s = input()[:-1]

print('Yes' if re.fullmatch(
    '[0-9]{' + str(a) + '}-[0-9]{' + str(b) + '}', s) != None else 'No')
