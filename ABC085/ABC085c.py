import sys
sys.setrecursionlimit(20000)

n, y = map(int, input().split())

memo = {}


def unchi(maisu, kane, a, b, c):
    if(maisu == 0):
        if(kane == 0):
            return [a, b, c]
        else:
            return False
    elif(kane < 1000):
        return False

    if((maisu, kane) in memo):
        return memo[(maisu, kane)]

    resultI = unchi(maisu - 1, kane - 10000, a + 1, b, c)
    if (resultI):
        memo[(maisu, kane)] = resultI
        return resultI
    resultI = unchi(maisu-1, kane-5000, a, b+1, c)
    if(resultI):
        memo[(maisu, kane)] = resultI
        resultI[1] -= 1
        return resultI
    resultI = unchi(maisu-1, kane-1000, a, b, c+1)
    if(resultI):
        memo[(maisu, kane)] = resultI
        resultI[2] -= 1
        return resultI
    memo[(maisu, kane)] = False
    return False


result = unchi(n, y, 0, 0, 0)
print(memo)
if(result):
    print(*result)
else:
    print(-1, -1, -1)
