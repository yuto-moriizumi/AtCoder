# AGC026c
def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # map(int, input().split())

    n = int(input())
    s = input()[:-1]
    from itertools import combinations

    ans = 0
    for i in combinations(range(n), n//2):
        sR = ''
        sB = ''
        for j in range(n):
            if j in i:
                sR += s[j]
            else:
                sB += s[j]
        print(sR, sB[::-1])
        if sR == sB[::-1]:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
