a, b = input().split()
print(max(
    int('9'+a[1:])-int(b),
    int(a[0]+'9'+a[2])-int(b),
    int(a[:2]+'9')-int(b),
    int(a)-int('1'+b[1:]),
    int(a)-int(b[0]+'0'+b[2]),
    int(a)-int(b[:2]+'0')
))
