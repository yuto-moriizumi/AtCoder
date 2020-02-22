# ABC078a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

x, y = input()[:-1].split()
alphabet = list('abcdefghijklmnopqrstuvwxyz'.upper())

if alphabet.index(x) < alphabet.index(y):
    print('<')
elif x == y:
    print('=')
else:
    print('>')
