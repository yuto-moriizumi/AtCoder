# ABC152d


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)

    n = int(input())
    cou = 0
    for i in range(1, n + 1):
        if str(i)[-1] == '0':
            continue
        # print(i)
        if str(i)[0] == str(i)[-1]:
            cou += 1
        k = 2
        while True:
            b = int(str(i)[-1] + '0' * (k - 2) + str(i)[0])
            if b <= n:
                if k > 2:
                    if n - b > 10 ** (k - 1):
                        cou += 10 ** (k - 2)
                    else:
                        cou += (n - b)//10 + 1
                else:
                    cou += 1
                #print(i, k, cou)
                k += 1
                continue
            #print(i, cou)
            break
    print(cou)


if __name__ == '__main__':
    main()
