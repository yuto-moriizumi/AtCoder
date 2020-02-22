# AGC028a
def main():
    import sys
    from math import gcd
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    n, m = map(int, input().split())
    s = input()[:-1]
    t = input()[:-1]

    def lcm_base(a, b):
        return a * b // gcd(a, b)

    lcm = lcm_base(n, m)

    for i in range(0, max(len(s), len(t)), lcm):
        print(s[i], t[i])


if __name__ == '__main__':
    main()
