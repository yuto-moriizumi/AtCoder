# ABC001b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m = int(input())/1000
if m < 0.1:
    print('00')
    exit(0)
if m <= 5:
    if m*10 < 10:
        print('0'+str(int(m*10)))
        exit(0)
    print(int(m*10))
    exit(0)
if m <= 30:
    print(int(m+50))
    exit(0)
if m <= 70:
    print(int((m-30)//5+80))
    exit(0)
if m > 70:
    print(89)
