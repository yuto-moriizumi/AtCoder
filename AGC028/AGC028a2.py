# AGC028a
def main():
    n, m = map(int, input().split())
    s = input()
    t = input()
    from fractions import gcd

    def lcm_base(a, b):
        return a * b // gcd(a, b)

    l = lcm_base(len(s), len(t))

    for i in range(l, l*2, l):
        x = [-1]*i


if __name__ == '__main__':
    main()
