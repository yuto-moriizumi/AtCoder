import os

print("ABCのいくつ？")
s = input()

if not os.path.exists("ABC" + s):
    os.mkdir("ABC" + s)
    for i in ("a", "b", "c", "d", "e", "f"):
        f = open("ABC" + s + "/ABC" + s + i + ".py", "w", encoding="utf8")
        f.write(
            "# ABC" + s + i +
            """\n
def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    #再帰関数を使わない限りPypyで出すこと
    
    
if __name__ == '__main__':
    main()
"""
        )
        f.close()
else:
    print("ABC" + s + "はすでに存在します")
