# ABC111a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

print(input()[:-1].replace('1', 'a').replace('9', '1').replace('a', '9'))
