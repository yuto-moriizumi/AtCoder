n = list(map(int, input().split()))
b1 = max(n)
n[n.index(b1)] -= 1
print(b1+max(n))
