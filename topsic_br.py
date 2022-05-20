#数列の操作

N = int(input())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))
a = 0

for x in range(N):
        if A[x] != B[x]:
            a = a + abs(A[x] - B[x])

        if A[x] == B[x]:
            continue

print(a)