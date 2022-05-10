#タイピングの秒数算出

S = input()
N = [0] * len(S)
Q = "a", "s", "d", "f", "g", "h", "j", "k", "l"
a = 0

for x in range(len(S)):
    for y in range(len(Q)):
        N[x] = S[x]
        if N[x] == Q[y] :
            a = a + 1
            break
        
        if N[x] != Q[y] :
            a = a + abs(x-(x-1))
            
print(a)