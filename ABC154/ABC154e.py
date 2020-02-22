# ABC154e


def main():
    import sys
    import math
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # Ä‹AŠÖ”‚ğg‚í‚È‚¢ŒÀ‚èPypy‚Åo‚·‚±‚Æ

    n = int(input())
    k = int(input())
    ans = 0
    print(math.ceil(math.log10(n)))

    def calc(s):
        return 10**s.count('A')-s.count('A')

    for i in range(1, math.floor(math.log10(n)) + 2):
        cou0 = i - k
        if cou0 < 0:
            continue
        couOther = i - cou0
        if int('9' * couOther + '0' * cou0) > n:
            ans += n - int('1' + '0' * cou0 + '1' * (couOther-1))
            continue
        ans += 10 ** couOther - 1
    print(ans)


if __name__ == '__main__':
    main()
