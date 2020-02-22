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

    x.sort(reverse=True)
    # map(int,input().split())
    tadasii = [None]*n

    def dfs(i, tf):
        if tf != None and tadasii[i] != None and tadasii[i] != tf:
            return 1 - 10 ** 3
        if tadasii[i]:
            tansaku = []
            for p, j in x[i]:
                tadasii[j[0] - 1] = j[1]
                if j[1] == 1:
                    tansaku.append(j[0] - 1)
            an = 0
            for j in tansaku:
                an += dfs(j, True)
            return 1
        return 0

    ans = 0
    for i in range(n):
        ans += dfs(i, None)
    print(ans)


if __name__ == '__main__':
    main()
