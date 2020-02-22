# AGC009a
def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # map(int, input().split())
    n = int(input())

    a = list()
    b = list()
    for _ in range(n):
        aa, bb = map(int, input().split())
        a.append(aa)
        b.append(bb)

    ans = 0
    dif = 0
    for i in range(n-1, -1, -1):
        osu = b[i]-(a[i]+dif) % b[i] if (a[i]+dif) % b[i] != 0 else 0
        #print(a[i]+dif, b[i], osu, ans)
        ans += osu
        dif += osu
    print(ans)


if __name__ == '__main__':
    main()
