# ABC145c


def main():
    import sys
    import itertools
    import math
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    # map(int,input().split())
    n = int(input())
    town = [tuple(map(int, input().split())) for _ in range(n)]
    ans = 0

    def kyori(pos1, pos2):
        return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

    def permutations_count(n, r):
        return math.factorial(n) // math.factorial(n - r)

    for i in itertools.permutations(town, n):
        # print(i)
        t = 0
        for j in range(1, n):
            t += kyori(i[j - 1], i[j])
        # print(t)
        ans += t
    print(ans/math.factorial(n))


if __name__ == '__main__':
    main()
