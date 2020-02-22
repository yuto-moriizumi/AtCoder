# ABC135d
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

s = input()
s = s[:len(s)-1]


# def is13nobaisu(st):
#    red = []
#    blue = []
#   mode = True  # Trueが赤
#  for i in range(-1, -len(st), -3):
#        if(mode):
#           red.append(st[i-3:i])
#           mode = not mode
#       else:
#          blue.append(st[i-3:i])
#   mode = not mode
#  print(red)
# print(blue)


# print("3"+"5")
print(s[-1])


def keisan(st, dif, keta):
    print(st, end="")
    c = 0
    if (keta != 0 and int(st) % 13 == 5):
        c += 1
        print("Yeah", end="")
    print()
    if (keta > 2):
        return c
    if (s[-keta] == "?"):
        for i in range(0, 10):
            c += keisan(str(i) + st, dif, keta + 1)
    else:
        c += keisan(s[-keta] + st, dif, keta + 1)
    return c


print(keisan("", 0, 1))
