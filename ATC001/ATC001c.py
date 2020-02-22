#高速フーリエ変換
import sys
input = sys.stdin.readline

from scipy import signal

n=int(input())
a=[]
b=[]
for _ in range(n):
    at,bt=map(int,input().split())
    a.append(at)
    b.append(bt)
l=signal.fftconvolve(a,b)
print(0)
for i in l:
    print(int(i))