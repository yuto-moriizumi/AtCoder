# ABC137d
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

dp = dict()


def hataraku(sigoto, day):
    t = 0
    if (day == 0 or sigoto >= len(a)):
        return 0
    if (dp.get((sigoto, day)) != None):
        return dp[(sigoto, day)]
    if (day >= a[sigoto][0]):
        print(str(sigoto)+"とる")
        t = max(a[sigoto][1] + hataraku(sigoto + 1, day - 1),
                hataraku(sigoto + 1, day))
        # print(t)
        dp[(sigoto, day)] = t
        print(str(sigoto) + "とりおわった")
        if(sigoto != 0):
            return t
    print(str(sigoto)+"とらない")
    t = max(hataraku(sigoto + 1, day), t)
    dp[(sigoto, day)] = t
    print(str(sigoto)+"とらずおわった")
    return t


def uooooo(day, i, s):
    print(day, i, s)
    if (day == 0):
        return 0
    if (i >= len(a)):
        return 0
    if(day >= a[i][0]):
        return max((uooooo(day - 1, i + 1, s+"1") + a[i][1]), uooooo(day, i + 1, s+"0"))
    else:
        return uooooo(day, i+1, s+"0")

    # print(hataraku(0, m))
print(uooooo(m, 0, ""))
