def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    n, w, c = map(int, input().split())
    mono = dict()
    for _ in range(n):
        w, v, c = map(int, input().split())
        if mono.get(c) == None:
            mono[c] = list()
        mono[c].append([w, v])
    # dp[i][j][c]=i番目まで見て重さがj以下、色がc種類以下となるように選んだ時の価値の総和の最大値
    dp = [[[0]*(c+1) for j in range(w+1)] for i in range(n+1)]
    for k in mono.keys():
        for i in range(n):
            for j in range(n):


if __name__ == '__main__':
    main()
