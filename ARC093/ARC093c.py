# ARC093c
def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    from collections import Counter

    n = int(input())
    a = [0]
    a.extend(list(map(int, input().split())))
    a.append(0)
    # print(a)

    total = 0
    for i in range(1, n+2):
        total += abs(a[i]-a[i-1])
    # print(total)

    for j in range(1, n+1):
        if a[j-1] <= a[j] <= a[j+1] or a[j-1] >= a[j] >= a[j+1]:
            print(total)
            continue
        print(total-abs(a[j]-a[j-1])-abs(a[j+1]-a[j])+abs(a[j+1]-a[j-1]))


if __name__ == '__main__':
    main()
