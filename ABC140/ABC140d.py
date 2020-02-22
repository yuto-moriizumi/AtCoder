# ABC140d
import re
import sys
import time
start = time.time()
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
s = input()[:-1]


findings = re.findall('R+|L+', s)
score = [0]*len(findings)
for i in range(len(score)):
    score[i] = len(findings[i])
# print(score)

for _ in range(k):
    superscore = [0] * len(score)
    maxScore = 0
    maxScorePos = 0
    for i in range(len(score)):
        superscore[i] = score[i]
        if (i - 1 >= 0):
            superscore[i] += score[i - 1]
        if (i + 1 < len(score)):
            superscore[i] += score[i + 1]

    # print('superscore'+str(superscore))
    center = superscore.index(max(superscore))
    tempscore = score[center]
    if (center - 1 >= 0):
        tempscore += score[center - 1]
    if (center + 1 < len(score)):
        tempscore += score[center+1]
    score[max(0, center-1):min(len(score), center+2)] = [tempscore]
    # print(score)
    #print(time.time() - start)
    if (time.time() - start > 1.9):
        break

print(sum(score)-len(score))
