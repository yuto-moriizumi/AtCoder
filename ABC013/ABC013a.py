# ABC013a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

alphabet = list('abcdefghijklmnopqrstuvwxyz'.upper())
print(alphabet.index(input()[:-1])+1)
