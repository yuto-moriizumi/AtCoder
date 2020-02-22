import math
n, k = map(int, input().split())
a = list(map(int, input().split()))
print(math.ceil((n-a.count(min(a)))/(k-1)))
