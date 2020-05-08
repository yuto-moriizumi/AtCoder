# ABC165d


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    n, m, q = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(q)]

    b = []

    def create():
        if len(b) >= n:
            t = eval()
            return t
        an = 0
        s = b[-1] if len(b) > 0 else 1
        for j in range(s, m + 1):
            b.append(j)
            an = max(an, create())
            b.pop()
        return an

    def eval():
        ans = 0

        for l in a:
            if b[l[1]-1] - b[l[0]-1] == l[2]:
                ans += l[3]
        #print(b, ans)
        return ans

    print(create())


if __name__ == '__main__':
    main()
