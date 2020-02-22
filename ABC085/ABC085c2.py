import sys
sys.setrecursionlimit(20000)

n, y = map(int, input().split())

memo = {}


def unchi(maisu, kane, s):
    if(maisu == 0):
        if(kane == 0):
            return [0, 0, 0]
        else:
            return False
    elif(kane < 1000):
        return False

    if((maisu, kane) in memo):
        return memo[(maisu, kane)]

    if(s >= 10000):
        result1 = unchi(maisu - 1, kane - 10000, 10000)
        if (result1):
            result1[0] += 1
            memo[(maisu, kane)] = tuple(result1)
            return result1
    if(s >= 5000):
        result2 = unchi(maisu-1, kane-5000, 5000)
        if (result2):
            result2[1] += 1
            memo[(maisu, kane)] = tuple(result2)
            return result2
    if (kane == 1000 * maisu):
        result3 = [0, 0, maisu]
        memo[(maisu, kane)] = tuple(result3)
        return result3
    memo[(maisu, kane)] = False
    return False


result = unchi(n, y, 10000)
if(result):
    print(*result)
else:
    print(-1, -1, -1)
