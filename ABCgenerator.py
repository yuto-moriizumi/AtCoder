import os

for j in range(139):
    s = '{:03}'.format(j)
    if not os.path.exists("ABC" + s):
        os.mkdir("ABC" + s)
        for i in ("a", "b", "c", "d", "e", "f"):
            f = open("ABC" + s + "/ABC" + s + i + ".py", "w")
            f.write(
                "#ABC" + s + i +
                "\nimport sys\ninput = sys.stdin.readline\nsys.setrecursionlimit(10**6)\n"
            )
            f.close()
    else:
        print("ABC" + s + "はすでに存在します")
