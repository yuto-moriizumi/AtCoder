# ABC071b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

alphabet = 'abcdefghijklmnopqrstuvwxyz'

s = input()
for i in s:
    # print(i)
    alphabet = alphabet.replace(i, '')
print(alphabet[0] if len(alphabet) > 0 else 'None')
