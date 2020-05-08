# ABC164d
def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    s = input()
    n = len(s)-1
    c = 0

    def modinv(a, mod=10**9+7):
        return pow(a, mod - 2, mod)

    def combination(n, r, mod=10**9+7):
        r = min(r, n-r)
        res = 1
        for i in range(r):
            res = res * (n - i) * modinv(i+1, mod) % mod
        return res

    import math

    def c_count(n, r):  # 組み合わせ
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

    counter = [0] * 2019
    number = 0
    for i in range(n):
        # print(s[n-i-1])
        #number += int(s[n-i-1])*10**(i+1)
        number = int(s[n-i-1:])
        counter[number % 2019] += 1
    counter[0] += 1

    for i in range(len(counter)):
        num = counter[i]
        if num >= 2:
            c += c_count(num, 2)

    print(c)


if __name__ == '__main__':
    main()
