# ABC141d
import sys
import heapq
import math
import fractions
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a, b = map(int, input().split())
cd = []


def prime_decomposition(n):
    i = 2
    table = set()
    while i * i <= n:
        while n % i == 0:
            n /= i
            table.add(i)
        i += 1
    if n > 1:
        table.add(n)
    return table


print(len(prime_decomposition(a).intersection(prime_decomposition(b)))+1)
exit()

for i in range(1, fractions.gcd(a, b) + 1):
    if (a % i != 0 or b % i != 0):
        continue
    flag = True
    for j in cd:
        if (j == 1):
            continue
        if (i % j == 0):
            flag = False
            break
    if (flag):
        cd.append(i)
print(len(cd))
