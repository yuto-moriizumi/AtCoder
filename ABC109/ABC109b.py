# ABC109b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
words = set()
lastWord = ''
for i in range(n):
    word = input()[:-1]
    if (i != 0 and word[0] != lastWord[-1] or word in words):
        print('No')
        exit()
    lastWord = word
    words.add(word)
print('Yes')
