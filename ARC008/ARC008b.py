# ARC008b
def main():
    import sys
    # input = sys.stdin.readline
    import math
    sys.setrecursionlimit(10 ** 6)
    from collections import Counter

    n, m = map(int, input().split())
    name = Counter(list(input()))
    kit = Counter(list(input()))
    needed = 0
    if len(set(name.elements()) - set(kit.elements())) != 0:
        print(-1)
        exit(0)
    for i in name.most_common():
        needed = max(needed, math.ceil(i[1]/kit[i[0]]))
    print(needed)


if __name__ == '__main__':
    main()
