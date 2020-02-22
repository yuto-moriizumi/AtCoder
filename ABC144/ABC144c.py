# ABC144c


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    # map(int,input().split())
    n = int(input())

    def prime_factorize(n):
        a = []
        while n % 2 == 0:
            a.append(2)
            n //= 2
        f = 3
        while f * f <= n:
            if n % f == 0:
                a.append(f)
                n //= f
            else:
                f += 2
        if n != 1:
            a.append(n)
        return a
    aiu = prime_factorize(n)
    aiu.reverse()
    ans = [1, 1]

    for i in aiu:
        if ans[0] < ans[1]:
            ans[0] *= i
        else:
            ans[1] *= i
    print(sum(ans)-2)


if __name__ == '__main__':
    main()
