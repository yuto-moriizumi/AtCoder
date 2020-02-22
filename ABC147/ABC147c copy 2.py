# ABC147c


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    n = int(input())
    x = []
    aa = []
    for _ in range(n):
        a = int(input())
        aa.append(a)
        x.append((a, [list(map(int, input().split())) for _ in range(a)]))

    # map(int,input().split())
    tadasii = [None]*n

    # i番目の人を正直とするdfs
    def dfs(i, su):
        if tadasii[i] == False:
            return 1 - (10 ** 5)
        tadasii[i] = True
        an = su
        for j in range(x[i][0]):
            if x[i][1][j][1] == 1:
                if tadasii[x[i][1][j][0]-1] == True:
                    continue
                if tadasii[x[i][1][j][0]-1] == False:
                    return 1 - (10 ** 5)
                tadasii[x[i][1][j][0]-1] = True
                an += dfs(x[i][1][j][0] - 1, su + 1)
        for j in range(n):
            if tadasii[j] == None:
                tadasii[j] = True
                an += dfs(j, su + 1)
                tadasii[j] = None
        return an

    ans = 0
    for i in range(n):
        tadasii[i] = True
        if dfs(i, 1) > 0:
            ans = max(ans, tadasii.count(True))
        tadasii = [None]*n
    print(ans-1)


if __name__ == '__main__':
    main()
