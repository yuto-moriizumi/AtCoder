# ABC153d


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    h = int(input())

    def attack(n):
        if n == 1:
            return 1
        return 1+2*attack(n//2)

    print(attack(h))


if __name__ == '__main__':
    main()
