# ABC173b


def main():
    import sys
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    n = int(input())
    s = [input() for _ in range(n)]
    from collections import Counter
    d = Counter(s)
    for i in ['AC', "WA", "TLE", "RE"]:
        print(i, 'x', d[i])


if __name__ == '__main__':
    main()
