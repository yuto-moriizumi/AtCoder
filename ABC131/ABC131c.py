# 最初に入れておくとinputが早くなる
#import sys
from fractions import gcd
#input = sys.stdin.readline

a, b, c, d = map(int, input().split())
# warikireru = set()
# for i in range(b//c+1):
#    for j in range(b // d+1):
#        k = c ** i * d ** j
#        if(a <= k <= b):
#            warikireru.add(k)
# print(warikireru)
# print(b-a+1-len(warikireru))

k = int(c * d / gcd(c, d))
x1 = b-b//c-b//d+b//k
a -= 1
x2 = a - a // c - a // d + a // k
print(x1-x2)


#a, b, c, d = map(int, input().split())
#lcm = int(c*d/gcd(c, d))
#A = a-1
#x1 = A-A//c-A//d+A//lcm
#x2 = b-b//c-b//d+b//lcm
# print(x2-x1)

# 4,6,8 3
# 9 1
# 6

# 12,18,24,30,36 5
# 16,24,32,40 4
# 31
