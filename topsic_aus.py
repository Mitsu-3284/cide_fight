#ジャングルジム　

N = int(input())
A = list(map(int,input().split()))
a = 0

for x in range(N) :
    if A[x] == A[N-(x+1)] :
        continue
    
    if A[x] > A[N-(x+1)] :
        break

    if  A[N-(x+1)] > A[x] :
        A = list(reversed(A))
        break

for y in range(N) :
    if y == N-1 :
        break
    else :
        a = a + max(0, A[y+1] - A[y])

print(a)