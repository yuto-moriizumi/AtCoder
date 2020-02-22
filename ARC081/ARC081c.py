# ARC081c
def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    from collections import Counter
    import heapq

    n = int(input())

    def fun(i):
        return -int(i)

    a = heapq.heapify(list(map(fun, input().split())))

    while(True):
        nn = heapq.heappop()
        if ln != 1


if __name__ == '__main__':
    main()
