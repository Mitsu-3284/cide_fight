#凸

N = int(input())
A = list(map(int,input().split()))
a = "YES"

for x in range(N-2):
    for y in range(x+1,N-1):
        for z in range(y+1,N):
            if (A[x] + A[z] ) /2 >= A[y]:
                a = "NO"
                break
        else:
            continue
        break
    else:
        continue
    break

print(a)
