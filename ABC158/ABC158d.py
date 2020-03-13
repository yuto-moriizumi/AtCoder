# ABC158d


def main():
    import sys
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    s = input()
    q = int(input())
    query = [input().split() for _ in range(q)]

    mode = 0
    from collections import deque
    que = deque(list(s))
    for i in query:
        if len(i) == 1:
            mode = 1-mode
            continue
        f = int(i[1])
        if mode == 0:
            if f == 1:
                que.appendleft(i[2])
            else:
                que.append(i[2])
        else:
            if f == 1:
                que.append(i[2])
            else:
                que.appendleft(i[2])
    mode = 1 if mode == 0 else - 1
    # print(mode)
    qq = list(que)
    # print(qq[::-1])
    print(*(qq[::mode]), sep='')


if __name__ == '__main__':
    main()
