#互いに異なる 

N = int(input())
A = list(map(int,input().split()))

if len(set(A)) == len(A):
    print("Yes")

else :
    print("No")