def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    n, k = map(int, input().split())
    book = dict()
    for _ in range(n):
        c, g = map(int, input().split())
        if book.get(g) == None:
            book[g] = list()
        book[g].append(c)
    for key in book.keys():
        book[key].sort(reverse=True)
    num = [0]
    for i in book.keys():
        num.append(num[i-1]+len(book[i]))
    rbooks = dict()
    for i in book.keys():
        for j in range(len(book[i])):
            if rbooks.get(i) == None:
                rbooks[i] = [0]
            rbooks[i].append(rbooks[i][j]+book[i][j])
    # print(book)
    # print(rbooks)
    # print(num)
    # dp[i][j]=i番目までのジャンルでj冊本を売るときの最大価値
    dp = [[0]*(k+1) for _ in range(len(book)+1)]
    #
    for i in book.keys():
        for j in range(min(num[i]+1, k+1)):
            for m in range(min(j+1, len(book[i])+1)):  # そのジャンルで何冊売るか
                t = dp[i-1][j-m] + m * (m-1)+rbooks[i][m]
                dp[i][j] = max(dp[i][j], t)
    print(dp[-1][-1])


if __name__ == '__main__':
    main()
