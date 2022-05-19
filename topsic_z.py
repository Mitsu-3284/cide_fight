#約数の総和

N = int(input())

#↓これだと重い
#ans = 0
# for x in range(1,N+1):　０から始まるから１からその約数まで
    # for y in range(1,x+1):
        # if x % y == 0 :
            # ans = ans + y

#↓

# 1つの値について、その約数の和を出す関数
#関数の方が計算が軽くなるから
# a...求めたい値
def calc(a: int) -> int:
    
    j = 1
    t = 0
    while j * j <= a: #求めたい値がある数の２乗より下の条件下で　例）a=8 j=2
        if a % j == 0: #求める数字(a)がjの約数なら
            t = t + j #そのjを代入
            if j != a // j: #求める数字のjではない約数の時
                t = t + (a // j) #その約数を計上 例）４とか
            # jはiの約数であることが確定
        j = j + 1
    
    return t
    
x = 0
# 1〜Nまで約数を出していく
for i in range(1, N+1):
    x = x + calc(i) #関数として定義したものを呼び出す。

print(x)
