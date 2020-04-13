# ABC162d


def main():
    import sys
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    n = int(input())
    s = input()
    l = set(list('RGB'))
    cum = [[0]*(n+1) for _ in range(3)]
    for i in range(n):
        ind = -1
        if s[-i - 1] == 'R':
            ind = 0
        elif s[-i - 1] == 'G':
            ind = 1
        elif s[-i - 1] == 'B':
            ind = 2
        for j in range(3):
            cum[j][n - i-1] = cum[j][n - i]
        cum[ind][n - i-1] += 1
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                continue
            last = l.copy()
            last.discard(s[i])
            last.discard(s[j])
            ind = -1
            string = last.pop()
            if string == 'R':
                ind = 0
            elif string == 'G':
                ind = 1
            elif string == 'B':
                ind = 2
            ans += cum[ind][min(j+(j-i)+1, n)]+cum[ind][j+1] - \
                cum[ind][min(j+(j-i), n)]
    print(ans)


if __name__ == '__main__':
    main()
