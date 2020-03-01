class StarrySkyTree:
    INF = 0

    def __init__(self, n):
        """初期化 n:処理する区間の長さ"""
        super().__init__()
        self.LV = (n-1).bit_length()
        self.N0 = 2**self.LV
        self.data = [0]*(2*self.N0)
        self.lazy = [0]*(2*self.N0)

    def gindex(self, l, r):
        L = (l + self.N0) >> 1
        R = (r + self.N0) >> 1
        lc = 0 if l & 1 else (L & -L).bit_length()
        rc = 0 if r & 1 else (R & -R).bit_length()
        for i in range(self.LV):
            if rc <= i:
                yield R
            if L < R and lc <= i:
                yield L
            L >>= 1
            R >>= 1

    def propagates(self, *ids):
        """遅延伝搬処理"""
        for i in reversed(ids):
            v = self.lazy[i-1]
            if not v:
                continue
            self.lazy[2*i-1] += v
            self.lazy[2*i] += v
            self.data[2*i-1] += v
            self.data[2*i] += v
            self.lazy[i-1] = 0

    def update(self, l, r, x):
        """区間[l, r)にxを加算 O(logN)"""
        *ids, = self.gindex(l, r)
        self.propagates(*ids)

        L = self.N0 + l
        R = self.N0 + r
        while L < R:
            if R & 1:
                R -= 1
                self.lazy[R-1] += x
                self.data[R-1] += x
            if L & 1:
                self.lazy[L-1] += x
                self.data[L-1] += x
                L += 1
            L >>= 1
            R >>= 1
        for i in ids:
            self.data[i-1] = self.custom_func(self.data[2*i-1], self.data[2*i])

    def query(self, l, r):
        """区間[l, r)に対してcustom_funcした結果を返す O(logN)"""
        self.propagates(*self.gindex(l, r))
        L = self.N0 + l
        R = self.N0 + r

        s = self.INF
        while L < R:
            if R & 1:
                R -= 1
                s = self.custom_func(s, self.data[R-1])
            if L & 1:
                s = self.custom_func(s, self.data[L-1])
                L += 1
            L >>= 1
            R >>= 1
        return s

    def custom_func(self, *args):
        """処理したい関数を記述"""
        return max(args)


n = int(input())

kukans = []
hazis = set()
maxT = 0
for _ in range(n):
    s, t = map(int, input().split())
    hazis.add(s)
    hazis.add(t - 1)
    maxT = max(maxT, t)
    kukans.append((s, t))
tree = StarrySkyTree(maxT)
for s, t in kukans:
    tree.update(s, t, 1)
theM = tree.query(1, maxT)
kList = []
for i in hazis:
    kasanari = tree.query(i, i+1)
    if kasanari == theM:
        kList.append(i)
left = kList[0]
right = kList[-1]
kouho = []
for s, t in kukans:
    if s <= left and right < t:
        kouho.append((s, t))
ans = 10 ** 6
#print('ya', left, right)
if len(kouho) == 0:
    print(theM)
    exit(0)
for s, t in kouho:
    tree.update(s, t, -1)
    test = tree.query(1, maxT)
    #print(s, t, test)
    ans = min(ans, test)
    tree.update(s, t, 1)
print(ans)
