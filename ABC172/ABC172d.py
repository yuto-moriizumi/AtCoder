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

    def calcYakusu(n):
        #d = Counter(prime_factorize(n))
        waru = math.floor(n ** 0.5)
        yakusu_zu = []
        n2 = n
        while yakusu[n2][0] == -1:
            if waru == 1:
                break
            if n2 % waru == 0:
                n2 = n2 // waru
                yakusu_zu.append(waru)
            else:
                waru -= 1
        yakusu_zu.append(n2)

        tmp = Counter()
        for i in yakusu_zu:
            tmp += yakusu[i][1] if len(yakusu[i]
                                       [1]) > 0 else Counter([i])
        yakusu[n][1] = tmp
        yakusu[n][0] = 1
        for i in yakusu[n][1]:
            yakusu[n][0] *= (yakusu[n][1][i] + 1)
        return yakusu[n][0]

    yakusu = [[-1, Counter()] for _ in range(n+2)]
    yakusu[1] = [1, Counter()]
    yakusu[2] = [2, Counter([2])]
    ans = 0
    for i in range(1, n + 1):
        if yakusu[i][0] == -1:
            yakusu[i][0] = calcYakusu(i)
        ans += i*yakusu[i][0]
    print(ans)


if __name__ == '__main__':
    main()
