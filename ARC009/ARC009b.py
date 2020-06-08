# ARC009b
def main():
    import sys
    # input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)

    b = input().split()
    n = int(input())
    normal = '0123456789'
    num = []
    for i in range(n):
        j = input()
        num.append([j, j])
    for i in range(n):
        ns = ''
        for j in num[i][0]:
            ns += str(b.index(j))
        num[i] = [int(ns), num[i][1]]
    num.sort()
    # print()
    print(*[i[1] for i in num], sep='\n')


if __name__ == '__main__':
    main()
