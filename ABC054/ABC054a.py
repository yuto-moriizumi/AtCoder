# ABC054a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a, b = map(int, input().split())
card = [i for i in range(1, 15)]
card[0] = None
card[13] = 1
# Aprint(card)

if card.index(a) > card.index(b):
    print('Alice')
elif card.index(a) == card.index(b):
    print('Draw')
else:
    print('Bob')
