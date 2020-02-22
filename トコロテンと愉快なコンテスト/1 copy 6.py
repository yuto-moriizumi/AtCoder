def main():
    import sys
    import math
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # map(int, input().split())

    s = input()[:-1]
    sakai = s.replace('RL', 'R,L').split(',')
    kodomo = [0] * (len(s)+1)
    pos = [0] * (len(sakai)+1)
    for i in range(len(sakai)):
        seq = sakai[i]
        pos[i + 1] = len(seq)+pos[i]
    for i in range(len(sakai)):
        seq = sakai[i]
        kodomo[pos[i + 1]-1] += (seq.count('R')+1) // 2  # 相手の左端にいる
        kodomo[pos[i + 1]] += seq.count('R') // 2  # 自分の右端にいる
        kodomo[pos[i]] += (seq.count('L')+1) // 2
        kodomo[pos[i] - 1] += seq.count('L') // 2
        # print(kodomo)
    # print(sakai)
    # print(pos)
    print(*kodomo[:-1])


if __name__ == '__main__':
    main()
