def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    n, k = map(int, input().split())
    a = []
    ruiseki = [0]
    for j in range(n):
        i = int(input())
        a.append(i)
        ruiseki.append(i+ruiseki[j])

    print(a)
    print(ruiseki)

    # i-1番目まででwin回数勝ったときの高橋くんの期限が良い最大日数
    def dfs(i, win, su):
        if(i == n):
            return su
        ans = 0
        for j in range(min(a[i]+1, k-win)):
            print(i, win, su)
            if ruiseki[i] == 0 or (win+j)/ruiseki[i+1] > win/ruiseki[i]:
                print(((win+j)/ruiseki[i+1], win/ruiseki[i])
                      if ruiseki[i] != 0 else 0)
                ans = max(ans, dfs(i+1, win+j, su+1))
            else:
                ans = max(ans, dfs(i+1, win+j, su))

        return ans

    print(dfs(0, 0, 0))


if __name__ == '__main__':
    main()
