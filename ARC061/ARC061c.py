s = input()


def dfs(pos, last, su):
    if (pos > len(s)):
        if (last < pos < len(s)):
            su += int(s[last:pos])
        return su
    # +を入れ無い場合

    non = dfs(pos + 1, last, su)
    # +を入れる場合
    print(pos, last, su)
    yes = dfs(pos + 1, pos, su + int(s[last:pos]))
    print('ya', non, yes, non+yes)
    return non+yes


print(dfs(1, 0, 0))
