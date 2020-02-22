# ABC008b
from collections import Counter
import sys
sys.setrecursionlimit(10**6)

n = int(input())
s = [input() for _ in range(n)]
print(Counter(s).most_common()[0][0])
