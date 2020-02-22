# 最初に入れておくとinputが早くなる
import sys
input = sys.stdin.readline

W, H, x, y = map(int, input().split())
flag = 0
if (W / 2 == x and H / 2 == y):
    flag = 1

print(min(max(x, W-x)*H, max(y, H-y)*W), flag)
