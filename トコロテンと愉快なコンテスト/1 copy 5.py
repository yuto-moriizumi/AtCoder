def main():
    import sys
    import math
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # map(int, input().split())

    n = int(input())
    wow = dict()
    for _ in range(n):
        s = list(input()[:-1])
        s.sort()
        s = str(s)
        if wow.get(s) == None:
            wow[s] = 0
        wow[s] += 1
    # print(wow)

    def combinations_count(n, r):
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
    ans = 0
    for i in wow.values():
        # print(i)
        if i == 1:
            continue
        ans += combinations_count(i, 2)
    print(ans)


if __name__ == '__main__':
    main()
