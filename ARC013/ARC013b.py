# ARC013b
def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)

    c = int(input())
    m = [list(map(int, input().split())) for _ in range(c)]

    aa = 0
    bb = 0
    cc = 0

    for i in m:
        ii, jj, kk = sorted(i)
        aa = max(aa, ii)
        bb = max(bb, jj)
        cc = max(cc, kk)

    print(aa*bb*cc)


if __name__ == '__main__':
    main()
