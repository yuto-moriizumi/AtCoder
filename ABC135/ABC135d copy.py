# ABC135d
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

st = input()[:-1]


def keisan(s):
    if (len(s) > 3):
        l = keisan(s[-3:])
        return l
    l = set()
    for i in range(0, 10):
        if (s[-1] != "?" and int(s[-1]) != i):
            continue
        for j in range(0, 10):
            if (len(s) < 2):
                j = 0
            elif (s[-2] != "?" and int(s[-2]) != j):
                continue
            for k in range(0, 10):
                if (len(s) < 3):
                    k = 0
                elif (s[-3] != "?" and int(s[-3]) != k):
                    continue
                if ((k * 100 + j * 10 + i) % 13 == 5):
                    l.add(k * 100 + j * 10 + i)
    return l


print(keisan(st))
