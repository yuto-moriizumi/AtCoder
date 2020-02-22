import os

for j in range(41):
    s = '{:03}'.format(j)
    if not os.path.exists("AGC" + s):
        os.mkdir("AGC" + s)
        for i in ("a", "b", "c", "d", "e", "f"):
            f = open("AGC" + s + "/AGC" + s + i + ".py", "w")
            f.write(
                "#AGC" + s + i + """\ndef main():
    import sys
    input=sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # map(int, input().split())

if __name__ == '__main__':
    main()"""
            )
            f.close()
    else:
        print("AGC" + s + "はすでに存在します")
