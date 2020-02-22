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

    a = list(map(fun, input().split()))
    heapq.heapify(a)

    b = []
    heapq.heapify(b)
    ln = 0
    cou = 0
    mn = 0
    while(len(a) > 0):
        i = -heapq.heappop(a)
        # print(i)
        if ln != i:
            ln = i
            cou = 0
        cou += 1
        if cou > 1:
            heapq.heappush(b, -i)
            cou = 0
    try:
        print(heapq.heappop(b)*heapq.heappop(b))
    except:
        print(0)


if __name__ == '__main__':
    main()
