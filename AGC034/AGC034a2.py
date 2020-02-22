# AGC034a
def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    n, a, b, c, d = map(int, input().split())
    s = list(input()[:-1])
    a -= 1
    b -= 1
    c -= 1
    d -= 1

    if c > d:
        flag = -1
        for i in range(max(2, b), min(n, d+1)):
            if s[i-2] == '.' and s[i-1] == '.' and s[i] == '.':
                flag = i-1
                break
            print('No')
            exit(0)

    else:
        while(b != d):
            if b+2 < n and b+2 <= d and s[b+2] == '.':
                b += 2
                continue
            if b+1 < n and b+1 <= d and s[b+1] == '.':
                b += 1
                continue
            print('No')
            exit(0)
        while(a != c):
            if s[a+2] == '.':
                a += 2
                continue
            if s[a+1] == '.':
                a += 1
                continue
            print('No')
            exit(0)
        print('Yes')


if __name__ == '__main__':
    main()
