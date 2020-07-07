# ABC172d


from collections import Counter


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    n = int(input())

    def prime_factorize(n):  # 因数分解
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
    import math

    ans2 = 0
    for i in range(1, n + 1):
        d = Counter(prime_factorize(i))
        ans = 1
        for j in d:
            ans *= d[j] + 1
        ans2 += i*ans
    print(ans2)


if __name__ == '__main__':
    main()
