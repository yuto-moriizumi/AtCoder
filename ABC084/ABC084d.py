# ABC084d
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

q = int(input())
query = []
rightest = 0
for _ in range(q):
    l, r = map(int, input().split())
    query.append((l, r))
    rightest = max(rightest, r)

isPrime = [False]*(rightest+1)
isPrime[2] = True


def prime_numbers(right):
    pn = [2]
    for L in range(3, right):
        chk = True
        for L2 in pn:
            if L % L2 == 0:
                chk = False
        if chk == True:
            # pn.append(L)
            isPrime[L] = True
    # return pn


prime_numbers(rightest+1)

ruiseki = [0]
for i in range(rightest+1):
    if i % 2 == 1 and isPrime[i] and isPrime[(i+1)//2]:
        ruiseki.append(ruiseki[i]+1)
    else:
        ruiseki.append(ruiseki[i])

print(isPrime)
print(ruiseki)
for l, r in query:
    print(ruiseki[r-1]-ruiseki[l+1])
