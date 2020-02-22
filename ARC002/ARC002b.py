# ARC002b
from datetime import date
from datetime import timedelta


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)

    y, m, d = map(int, input().split('/'))

    dat = date(y, m, d)

    for i in range(10 ** 10):
        if dat.year % (dat.month * dat.day) == 0:
            print(*(dat.__str__().split('-')), sep='/')
            exit(0)
        dat += timedelta(days=1)


if __name__ == '__main__':
    main()
