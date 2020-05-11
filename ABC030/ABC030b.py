# ABC030b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
zikan = n % 12 / 12*360
hun = m / 60*360
zikan = n % 12 / 12 * 360+m/60 % 12 / 12 * 360

if zikan >= hun:
    dis = zikan - hun
    dis2 = 360 - zikan + hun
else:
    dis = hun-zikan
    dis2 = 360 - hun + zikan
print(min(dis, dis2))
