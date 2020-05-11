# ABC167d


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    pos = [-1] * n
    pos[0] = 0

    nex = a[0] - 1
    now = 0
    turn = 0

    mode = False

    while True:
        if not mode and pos[nex] == -1:
            pos[nex] = pos[now] + 1
            now = nex
            nex = a[nex] - 1
            turn += 1
            continue
        res = ((k-turn) % (turn - pos[nex] + 1)+turn) % (turn - pos[nex] + 1)
        for i in range(n):
            if pos[i] == res:
                print(i + 1)
                exit(0)
    # print(pos)


if __name__ == '__main__':
    main()
