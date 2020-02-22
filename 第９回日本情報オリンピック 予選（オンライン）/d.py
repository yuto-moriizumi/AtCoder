import itertools

n = int(input())
k = int(input())
card = [input() for _ in range(n)]

lis = set()

#print(len(set([i.join() ])))

print(len(set([''.join(i) for i in itertools.permutations(card, k)])))


def dfs(pos, st, cnt):
    if (cnt == k):
        lis.add(st)
        return
    if (pos >= n):
        return
    #print(pos, st, cnt)
    dfs(pos + 1, st+card[pos], cnt + 1)
    dfs(pos + 1, st, cnt)


#dfs(0, '', 0)
# print(lis)
