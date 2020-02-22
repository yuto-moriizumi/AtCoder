# 最初に入れておくとinputが早くなる
import sys
input = sys.stdin.readline

# スタック最大数をセット
sys.setrecursionlimit(10**6)

n, a, b = map(int, input().split())
print(min(a*n, b))
