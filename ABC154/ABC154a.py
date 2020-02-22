# ABC154a


def main():
    import sys
    sys.setrecursionlimit(10**6)
    # Ä‹AŠÖ”‚ğg‚í‚È‚¢ŒÀ‚èPypy‚Åo‚·‚±‚Æ

    s, t = input().split()
    a, b = map(int, input().split())
    u = input()
    if s == u:
        a -= 1
    if t == u:
        b -= 1
    print(a, b)


if __name__ == '__main__':
    main()
