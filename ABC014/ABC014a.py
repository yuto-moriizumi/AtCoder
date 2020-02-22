# ABC014a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a = int(input())
b = int(input())
print(b-a % b if a % b != 0 else 0)
