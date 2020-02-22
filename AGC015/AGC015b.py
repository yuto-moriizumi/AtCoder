# AGC015b
def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # map(int, input().split())

    s = input()[:-1]
    n = len(s)
    ans = 0
    for i in range(n):
        if s[i] == 'U':
            ans += (n-i-1)+i*2
        else:
            ans += i+(n-i-1)*2
    print(ans)


if __name__ == '__main__':
    main()
