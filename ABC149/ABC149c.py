# ABC149c


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    # map(int,input().split())
    x = int(input())

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

    for i in range(x, x * x):
        if len(prime_factorize(i)) < 2:
            print(i)
            exit(0)


if __name__ == '__main__':
    main()
