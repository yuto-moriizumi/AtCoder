# 最初に入れておくとinputが早くなる
#import numpy as np
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
azi = []
minn = n+l-1
for i in range(1, n+1):
    azi.append(i + l - 1)
    if (abs(minn) >= abs(i + l - 1)):
        minn = i + l - 1
print(sum(azi)-minn)
#arr = np.array(azi)
#ab = np.abs(arr)

#print(sum(azi) - azi[np.where(ab == ab.min()).tolist()[0]])
