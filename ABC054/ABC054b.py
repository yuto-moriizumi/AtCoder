#ABC054b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]


def match(x, y):
    for i in range(m):
        for j in range(m):
            if (a[y + i][x + j] != b[i][j]):
                return False
    return True


for i in range(n - m + 1):
    for j in range(n - m + 1):
        if (a[i][j] == b[0][0] and match(i, j)):
            print("Yes")
            exit(0)
print("No")