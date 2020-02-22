import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

h, w = map(int, input().split())
s = []
for _ in range(h):
    s.append(input())

result = 0
memo = {}


def terasu(x, y, d):
    #print(x, y, h, w)
    if y < 0 or x < 0 or y >= h or x >= w:
        return 0
    # if (x, y) in memo.keys():
    #    return 0
    if s[y][x] == "#":
        return 0
    #memo[(x, y)] = True
    if d == "f":
        return 1 + terasu(x + 1, y, "e") + terasu(x, y - 1, "s") + terasu(x, y+1, "n") + terasu(x-1, y, "w")
    elif d == "e":
        if (memo.get((x, y, "e")) != None):
            return memo[(x, y, "e")]
        memo[(x, y, "e")] = 1 + terasu(x + 1, y, "e")
        return memo[(x, y, "e")]
    elif d == "s":
        if (memo.get((x, y, "s")) != None):
            return memo[(x, y, "s")]
        memo[(x, y, "s")] = 1 + terasu(x, y+1, "s")
        return memo[(x, y, "s")]
    elif d == "n":
        if (memo.get((x, y, "n")) != None):
            return memo[(x, y, "n")]
        memo[(x, y, "n")] = 1 + terasu(x, y-1, "n")
        return memo[(x, y, "n")]
    elif d == "w":
        if (memo.get((x, y, "w")) != None):
            return memo[(x, y, "w")]
        memo[(x, y, "w")] = 1 + terasu(x - 1, y, "w")
        return memo[(x, y, "w")]


for y in range(h):
    for x in range(w):
        result = max(result, terasu(x, y, "f"))
print(result-4)
