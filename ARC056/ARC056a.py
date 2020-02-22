a, b, k, l = map(int, input().split())
if b/l < a:
    print(min((k-k//l*l)*a+k//l*b, (k//l+1)*b))
else:
    print(a*k)
