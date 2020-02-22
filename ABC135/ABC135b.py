# ABC135b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
p = list(map(int, input().split()))

last = 0
for i in range(1, len(p)):
    if (p[i] < p[i - 1]):
        # print("swapneeded"+str(i))
        if (last == 0 or last == i - 1):
            #print("swaped" + str(i))
            temp = p[i]
            p[i] = p[i - 1]
            p[i-1] = temp
            last = i
        else:
            print("NO")
            exit()
print("YES")
