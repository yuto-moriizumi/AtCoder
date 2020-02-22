# ABC149d


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()[:-1]
    flag = [False]*n
    # dp[i][T][J]=k手前にJを出してi番目でTを出すときの最高得点
    # dp[i][0][1]=dp[i-1][0][1]

    def tokuten(aite):
        if aite == 'r':
            return p
        if aite == 's':
            return r
        if aite == 'p':
            return s

    ans = t.count('r')*tokuten('r')+t.count('s') * \
        tokuten('s')+t.count('p')*tokuten('p')
    for i in range(n):
        if i - k >= 0 and t[i] == t[i - k] and not flag[i-k]:
            ans -= tokuten(t[i])
            flag[i] = True
    print(ans)


if __name__ == '__main__':
    main()
