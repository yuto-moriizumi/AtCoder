# ABC146a


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    # map(int,input().split())
    yo = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    #n = int(input())
    s = input()[:-1]
    if yo.index(s) == 0:
        print(7)
    else:
        print(7-yo.index(s))


if __name__ == '__main__':
    main()
