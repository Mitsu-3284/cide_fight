#品切れ　

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

for x in range(N):
    if A[x] < B[x] :
        print(x+1)