# ABC168e


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))
    import math

    def c_count(n, r):  # 組み合わせ
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

    from collections import Counter
    n = int(input())
    LL = []
    for _ in range(n):
        a, b = map(int, input().split())
        LL.append(min(abs(a / b), abs(b / a)))
    LL = Counter(LL)
    ans = 0
    for i, v in LL.most_common():
        ans += (2**v-v)*2**(len(LL)-1)
        print(i, v)
    print(ans)


if __name__ == '__main__':
    main()
