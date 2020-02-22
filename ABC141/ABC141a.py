# ABC141a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

s = input()

w = ['Sunny', 'Cloudy', 'Rainy']

print(w[(w.index(s[:-1])+1) % 3])
