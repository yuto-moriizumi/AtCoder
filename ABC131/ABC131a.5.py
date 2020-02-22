#最初に入れておくとinputが早くなる
import sys
input = sys.stdin.readline

#スタック最大数をセット
sys.setrecursionlimit(10**6)

#メモ
#listは遅い set最速 dict次点 listが最遅

#二次元リスト
#[[0]*w for _ in range(h)]

#numpyの選択
#a=
#[[ 0  1  2  3]
# [ 4  5  6  7]
# [ 8  9 10 11]] この行列に対して

#a[1:,1:3]は
#[[5 6
#  9 10]]
#詳しくはABC129d.2を参照