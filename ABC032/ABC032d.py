# ABC032d
# from subprocess import*
# call(('pypy3', '-c', """


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    n, w = map(int, input().split())
    luggage = []
    maxValue = 0
    sumValue = 0
    for _ in range(n):
        v, weight = map(int, input().split())
        luggage.append([v, weight])
        maxValue = max(maxValue, v)
        sumValue += v

    if n <= 30:  # :
       # nが小さいので全探索
        def dfs(i, wei):
            if(i == n):
                return 0
            # print('a', i, wei, w-wei, luggage[i][1])
            if(w-wei >= luggage[i][1]):
                return max(dfs(i+1, wei), dfs(i+1, wei+luggage[i][1])+luggage[i][0])
            return dfs(i+1, wei)
        print(dfs(0, 0))
        exit(0)
    if maxValue < w:  #
        # 価値が小さいので添字に価値を入れたdp
        dp = [[9999999999]*(sumValue + 2) for _ in range(n+2)]
        dp[0][0] = 0
        ansIdx1 = 0
        ansIdx2 = 0
        for i in range(1, n+1):
            for j in range(sumValue+1):
                if(j-luggage[i-1][0] >= 0):
                    dp[i][j] = min(dp[i-1][j-luggage[i-1][0]] +
                                   luggage[i-1][1], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
                if(dp[i][j] <= w and ansIdx2 < j):
                    ansIdx1 = i
                    ansIdx2 = j
                    # print(dp[i][j])
        # print(dp)
        print(ansIdx2)
        exit(0)

    # 重さが小さいので添字に重さを入れたdp
    # dp[i][w]=i番目以降で重さw以下での価値の和の最大値
    # dp[i][w]=dp[i+1][w] 選ばないとき
    # dp[i][w]=max(dp[i+1][w-W[i]]+V[i],dp[i+1][w]) 選ぶとき
    dp = [[0]*(w + 2) for _ in range(n+2)]

    for i in range(n-1, -1, -1):
        for j in range(w+1):
            if(j-luggage[i][1] >= 0):
                dp[i][j] = max(dp[i+1][j-luggage[i][1]] +
                               luggage[i][0], dp[i+1][j])
            else:
                dp[i][j] = dp[i+1][j]
    # print(dp)
    print(dp[0][w])


if __name__ == '__main__':
    main()
# """))
