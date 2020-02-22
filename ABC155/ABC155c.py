# ABC155c


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    n = int(input())
    s = [input()[:-1] for _ in range(n)]
    from collections import Counter
    ma = 0
    ans = []
    for st, cou in Counter(s).most_common():
        ma = max(ma, cou)
        if cou == ma:
            ans.append(st)
        else:
            break
    ans.sort()
    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
