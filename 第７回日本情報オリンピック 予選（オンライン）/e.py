r, c = map(int, input().split())
mochi = [list(map(int, input().split())) for _ in range(r)]
uragaesu = [False]*r


def dfs(i):
    if i == r:
        return calc()
    uragaesu[i] = True
    ans = dfs(i+1)
    uragaesu[i] = False
    return max(ans, dfs(i+1))


def calc():
    cou = 0
    for i in range(c):
        cou2 = 0
        for j in range(r):
            moc = mochi[j][i]
            if uragaesu[j]:
                moc = 1-moc
            cou2 += moc
        cou += max(r - cou2, cou2)
    return cou


print(dfs(0))
