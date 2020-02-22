# ABC147b


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    # map(int,input().split())
    s = input()[:-1]
    ans = 0
    for i in range(len(s) // 2):
        if s[i] != s[-i-1]:
            #print(s[i], s[-i-1])
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()