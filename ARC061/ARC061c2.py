s = input()


def dfs(pos, fm):
    if (pos >= len(s)):
        #print(pos, fm, eval(fm))
        return eval(fm)
    #print(pos, fm)
    return dfs(pos+1, fm+s[pos])+dfs(pos+1, fm+'+'+s[pos])


print(dfs(0, '')//2)
