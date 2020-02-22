# ABC104c
import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

d, g = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(d)]
toku = [False]*d
# 全完を2^D通り探索


def dfs(i, su, cnt):
    #print(i, su, cnt)
    if (i >= d):
        if (su >= g):  # 目標点を超えている場合
            return cnt
        # 超えていない場合は、全完していない問題のうち一番点数が高い物を解いていこう
        for j in range(d - 1, -1, -1):
            if (toku[j]):
                continue
            # j問目はp[j][0]問しかないので、それ以上解くことはできない
            tokuzo = min(p[j][0], math.ceil((g - su) / (100 * (j + 1))))
            if (su + 100 * (j + 1) * tokuzo >= g):  # 目標点を超えたら
                return cnt + tokuzo
            return 99999  # 目標点が超えられなかった

    # i問目を全完する場合としない場合
    toku[i] = True
    suru = dfs(i + 1, su + (i + 1) * p[i][0]
               * 100 + p[i][1], cnt + p[i][0])
    toku[i] = False
    sinai = dfs(i + 1, su, cnt)
    # print(i, suru, sinai)
    return min(suru, sinai)


print(dfs(0, 0, 0))
