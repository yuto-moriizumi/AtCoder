#from subprocess import*
# call(('pypy3', '-c', """


def main():
    n, m = map(int, input().split())
    dp = [[[0]*102 for i in range(102)] for j in range(102)]
    for _ in range(n):
        x, y, z, w = map(int, input().split())
        dp[x][y][z] = max(w, dp[x][y][z])
    applicant = [list(map(int, input().split())) for _ in range(m)]

    for x in range(101):
        for y in range(101):
            for z in range(101):
                dp[x+1][y][z] = max(dp[x+1][y][z], dp[x][y][z])
                dp[x][y+1][z] = max(dp[x][y+1][z], dp[x][y][z])
                dp[x][y][z+1] = max(dp[x][y][z+1], dp[x][y][z])
    for i in applicant:
        print(dp[i[0]][i[1]][i[2]])


if __name__ == '__main__':
    main()
# """))
