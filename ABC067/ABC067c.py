# ABC067c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))


def cum(array):
    result = [0]
    for i in range(len(array)):
        result.append(array[i]+result[i])
    return result


cumArray = cum(a)
#print(cumArray)

ans = 10**12
for i in range(1, n):
    # print(i, cumArray[i], cumArray[n]-cumArray[i],
    #      abs(cumArray[n]-2*cumArray[i]))
    ans = min(ans, abs(cumArray[n]-2*cumArray[i]))

print(ans)
