#タイピングの秒数算出

S = input()
Q = ['a', 's', 'd', 'f', 'g','h', 'j', 'k', 'l']
def v(s_key: str, e_key: str ) -> int:
    return abs(Q.index(s_key) - Q.index(e_key))
# print("タイピングしたい文字列={}".format(S))
a = 0
b = 1

for i,str in enumerate(S):
    if i == 0:
        d = v('a', str)
    else:
        d = v(S[i - 1], str)
# print("距離={}".format(distance))
    a += d
    a += b

print(a)