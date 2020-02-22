def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    w, h = map(int, input().split())
    U = [[[0]*2 for i in range(w+2)] for j in range(h+2)]
    R = [[[0]*2 for i in range(w+2)] for j in range(h+2)]
    MOD = 10**5
    # U[i][j][k]=i,jに上向きに到達する経路の個数（k=0の時はここで曲がれる）
    U[1][0][0] = 1
    R[0][1][0] = 1

    for i in range(h+1):
        for j in range(w+1):
            U[i+1][j][0] += U[i][j][0]+U[i][j][1]
            U[i+1][j][1] += R[i][j][0]
            R[i][j+1][0] += R[i][j][0]+R[i][j][1]
            R[i][j+1][1] += U[i][j][0]
    print((sum(U[h-1][w-1])+sum(R[h-1][w-1])) % MOD)


if __name__ == '__main__':
    main()
