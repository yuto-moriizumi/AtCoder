n, m = map(int, input().split())
switches = []
for _ in range(m):
    switches.append(list(map(int, input().split()))[1:])
p = list(map(int, input().split()))

ans = 0
switchState = [0]*n


def dfs(i, tukeru):
    #print(i, tukeru)
    if(i == n):
        sumOfTento = 0
        for denkyu in range(m):
            sumOfswitch = 0
            for switch in switches[denkyu]:
                sumOfswitch += switchState[switch-1]
            if(sumOfswitch % 2 == p[denkyu]):
                sumOfTento += 1
        # print(switchState)
        if(sumOfTento == m):
            return 1
        else:
            return 0
    switchState[i] = tukeru
    return dfs(i+1, 0) + (dfs(i+1, 1) if i != n-1 else 0)


print(dfs(0, 0)+dfs(0, 1))
