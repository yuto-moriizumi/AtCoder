# ARC022a
def main():
    s = input()
    n = len(s)
    for i in range(n - 2):
        for j in range(i, n - 1):
            for k in range(j, n):
                if (s[i] == 'I' or s[i] == 'i') and (s[j] == 'C' or s[j] == 'c') and (s[k] == 't' or s[k] == 'T'):
                    print('YES')
                    #print(s[i], s[j], s[k])
                    exit(0)
    print('NO')


if __name__ == '__main__':
    main()
