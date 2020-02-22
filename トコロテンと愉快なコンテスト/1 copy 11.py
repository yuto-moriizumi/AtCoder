def main():
    import sys
    import heapq
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    n, m = map(int, input().split())
    worked = [False]*m

    q = []
    heapq.heapify(q)

    for _ in range(n):
        a, b = map(int, input().split())
        heapq.heappush(q, (-b, a))

    ans = 0
    while (m >= 0 and len(q) > 0):
        value, nissu = heapq.heappop(q)
        #value = work[0]
        #nissu = work[1]
        #print(value, nissu)
        while(True):
            if m - nissu >= 0:
                if worked[m - nissu]:
                    nissu += 1
                    continue
                # print('work')
                ans += -value
                worked[m-nissu] = True
                #print(ans, m)
            break
    print(ans)


if __name__ == '__main__':
    main()
