# ABC025c


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    b = [list(map(int, input().split())) for _ in range(2)]
    c = [list(map(int, input().split())) for _ in range(3)]

    banmen = [['*']*3 for _ in range(3)]

    def calc():
        score = 0
        # b[2][3]についての直大の得点
        for i in range(2):
            for j in range(3):
                if banmen[i][j] == banmen[i+1][j]:
                    score += b[i][j]
        # c[3][2]についての直大の得点
        for i in range(3):
            for j in range(2):
                if banmen[i][j] == banmen[i][j+1]:
                    score += c[i][j]
        return score

    # ミニマックス法
    def dfs(turn):
        if turn == 9:
            return calc()
        if turn % 2 == 0:
            Max = -1
            for i in range(3):
                for j in range(3):
                    if banmen[i][j] != '*':
                        continue
                    banmen[i][j] = '〇'
                    Max = max(Max, dfs(turn+1))
                    banmen[i][j] = '*'
            return Max
        else:
            Min = 10**9
            for i in range(3):
                for j in range(3):
                    if banmen[i][j] != '*':
                        continue
                    banmen[i][j] = '×'
                    Min = min(Min, dfs(turn+1))
                    banmen[i][j] = '*'
            return Min

    chokudai = dfs(0)
    print(chokudai)
    Sum = 0
    for i in b:
        Sum += sum(i)
    for i in c:
        Sum += sum(i)
    print(Sum-chokudai)


if __name__ == '__main__':
    main()
