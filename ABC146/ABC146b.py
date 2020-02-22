# ABC146b


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    # map(int,input().split())
    alphabet = list('abcdefghijklmnopqrstuvwxyz'.upper())
    # print('abcdefghijklmnopqrstuvwxyz'.upper().index('A'))
    n = int(input())
    s = input()[:-1]
    # print(alphabet)
    for i in s:
        #print(i, alphabet.index(i))
        print(alphabet[(alphabet.index(i)+n) % 26], end='')


if __name__ == '__main__':
    main()
