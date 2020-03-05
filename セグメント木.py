class SegmentTree:
    #####単位元######
    ide_ele = 10**12

    # num:n以上の最小の2のべき乗

    def segfunc(self, x, y):
        return min(x, y)  # 例としてmin関数を設定

    def __init__(self, n):
        super().__init__()
        self.num = 2**(n-1).bit_length()  # nは元々の配列の長さ
        self.seg = [self.ide_ele]*(2*self.num+1)

    def init(self, init_val):  # セグ木にしたい配列を渡す
        # set_val
        for i in range(len(init_val)):
            self.seg[i+self.num-1] = init_val[i]
        # built
        for i in range(self.num-2, -1, -1):
            self.seg[i] = self.segfunc(self.seg[2*i+1], self.seg[2*i+2])

    def update(self, k, x):
        k += self.num-1
        self.seg[k] = x
        while k:
            k = (k-1)//2
            self.seg[k] = self.segfunc(self.seg[k*2+1], self.seg[k*2+2])

    def query(self, p, q):
        if q <= p:
            return ide_ele
        p += self.num-1
        q += self.num-2
        res = self.ide_ele
        while q-p > 1:
            if p & 1 == 0:
                res = self.segfunc(res, self.seg[p])
            if q & 1 == 1:
                res = self.segfunc(res, self.seg[q])
                q -= 1
            p = p//2
            q = (q-1)//2
        if p == q:
            res = self.segfunc(res, self.seg[p])
        else:
            res = self.segfunc(self.segfunc(res, self.seg[p]), self.seg[q])
        return res
