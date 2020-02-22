import os

for j in range(104):
    s = '{:03}'.format(j)
    if not os.path.exists("ARC" + s):
        os.mkdir("ARC" + s)
        for i in ("c", "d", "e", "f"):
            f = open("ARC" + s + "/ARC" + s + i + ".py", "w")
            f.write(
                "#ARC" + s + i + """\ndef main():
    import sys
    input=sys.stdin.readline
    sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    main()"""
            )
            f.close()
    else:
        print("ARC" + s + "はすでに存在します")
