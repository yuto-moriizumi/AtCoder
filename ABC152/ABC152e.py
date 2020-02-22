# ABC152e


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)
    MOD = 10**9+7

    from fractions import gcd

    n = int(input())
    a = list(map(int, input().split()))

    ans = a[0]

    b = 1
    l = ans

    if n == 1:
        print(1)
        exit(0)

    for i in range(1, n):
        ans = ans * a[i] // gcd(ans, a[i])
        b *= (ans // l)
        # print(b)
        b += ans // a[i]
        #print(a[i], b, ans, l)
        l = ans
    # print(ans)
    o = ans
    # print(o)

    # for i in a:
    #    b += o//i % MOD
    print(b % MOD)


if __name__ == '__main__':
    main()
