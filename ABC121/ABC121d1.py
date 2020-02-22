import sys
input = sys.stdin.readline

a, b = map(int, input().split())
if(a % 2 == 0):
    if(b % 2 == 0):
        print((b-a)//2 % 2 ^ b)
    else:
        b += 1
        print((b-a)//2 % 2)
else:
    a += 1
    if(b % 2 == 0):
        print((b-a)//2 % 2 ^ b ^ (a-1))
    else:
        b += 1
        print((b-a)//2 % 2 ^ (a-1))
