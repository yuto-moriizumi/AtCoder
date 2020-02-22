#解説コードコピペです

import numpy as np
 
def solve():
    H, W = list(map(int, input().split()))
    grid = []
    for i in range(H):
        grid.append(list(input()))
    #print((np.array(grid) == ".") * 1) #行列演算 "." ならTrue そうでなければFalseの行列をつくる *1で1と0に変換
    grid = (np.array(grid) == ".") * 1  # ランプをおける:1, 障害物:0
 
    L = np.zeros((H,W), dtype=int) #0でうめつくした行列をつくる
    R = np.zeros((H,W), dtype=int)
    U = np.zeros((H,W), dtype=int)
    D = np.zeros((H,W), dtype=int)
    
    for j in range(W): #列単位で処理
        if j == 0:
            L[:, j] = grid[:, j]
        else:
            L[:, j] = (L[:, j-1] + 1) * grid[:, j] #gridでかけることで 障害物があったときにそのマスを0にする
    
    for j in range(W-1, -1, -1):
        if j == W-1:
            R[:, j] = grid[:, j]
        else:
            R[:, j] = (R[:, j+1] + 1) * grid[:, j]
 
    for i in range(H):
        if i == 0:
            U[i] = grid[i] * 1
        else:
            U[i] = (U[i-1] + 1) * grid[i]
    
    for i in range(H-1, -1, -1):
        if i == H-1:
            D[i] = grid[i]
        else:
            D[i] = (D[i+1] + 1) * grid[i]
 
    #print(L+R+U+D) 各行列をたして行列を返してくれますよ
    ans = np.max(L+R+U+D-3)
    print(ans)
 
 
if __name__ == "__main__": #ここはしらん
    solve()