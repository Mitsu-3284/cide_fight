#マス目の中に文字を追加

H, W, Q = map(int,input().split())
A = [["."] * W for x in range(H)]

for y in range(Q):
    r, c, s = map(str,input().split()) #一旦strで入力
    r = int(r) - 1  #rは数字にして（戻して）、行列は０から始まるから−１
    c = int(c) - 1  #上に同じ

    A[r][c] = s

for z in A : #行毎に出力
    print("".join(z)) #文字としてzに入った配列を連結して出力