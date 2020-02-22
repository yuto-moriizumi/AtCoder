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
    s[a] = '.'
    s[b] = '.'
    if b < a:
        t = b
        b = a
        a = t
        t = d
        d = c
        c = t
    while(b < d):
        if b+2 < n and b+2 < d and s[b+2] != '#':
            b += 2
            continue
        if s[b+1] != '#':
            b += 1
            continue
        print('No')
        exit(0)
    while(a < c):
        if a+2 < n and a+2 < c and s[a+2] != '#':
            a += 2
            continue
        if s[a+1] != '#':
            a += 1
            continue
        print('No')
        exit(0)
    print('Yes')


if __name__ == '__main__':
    main()
