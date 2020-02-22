# ABC062b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

h, w = map(int, input().split())
a = [input().replace('\n', '') for _ in range(h)]

print('#' * (w + 2))
for line in a:
    print('#', end='')
    print(line, end='')
    print('#')
print('#' * (w + 2))
