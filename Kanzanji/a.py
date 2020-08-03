h, w = map(int, input().split())
print(max(0, (w-1))*h+max(0, (h-1))*w)
