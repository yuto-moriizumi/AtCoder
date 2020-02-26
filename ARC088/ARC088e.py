# ARC088e
def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)

    class Bit:
        def __init__(self, n):
            self.size = n
            self.tree = [0] * (n + 1)

        def sum(self, i):
            s = 0
            while i > 0:
                s += self.tree[i]
                i -= i & -i
            return s

        def add(self, i, x):
            while i <= self.size:
                self.tree[i] += x
                i += i & -i

    s = input()[:-1]
    from collections import Counter
    c = Counter(s)
    t = 0
    for i in c.most_common():
        if i[1] % 2 == 1:
            t += 1
    if t != 0:
        if len(s) % 2 == 0 or t >= 1:
            print(-1)
            exit(0)

    neuString = [''] * len(s)
    


if __name__ == '__main__':
    main()
