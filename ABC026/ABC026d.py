# ABC026d
from math import sin
from math import pi
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
a, b, c = map(int, input().split())


def f(n):
    return a*n+b*sin(c*n*pi)


def evaluate(n):
    F = f(n)
    if F < 100:  # もっと高い値を探せ
        return 1
    if F == 100:  # まさにこの値
        return 0
    if F > 100:  # もっと低い値を探せ
        return - 1


def binary_search(low, high):
    lowest = low
    highest = high
    while 10**-12 <= high-low:
        mid = (low + high) / 2
        guess = evaluate(mid)
        if guess == 0:
            return [mid, mid]
        if guess < 0:
            high = mid
            highest = mid
        else:
            low = mid
            lowest = mid

    return [lowest, highest]


print(binary_search(0, (100+b)/a+1)[0])
