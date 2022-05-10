#右折　

N = int(input())
C = [""] * N
x, y = 0, 0

for a in range(N):
    C[a] = int(input())
    if (a + 1) % 4 == 1 :
        x = x + C[a]

    if (a + 1) % 4 == 2 :
        y = y - C[a]

    if (a + 1) % 4 == 3 :
        x = x - C[a]

    if (a + 1) % 4 == 0 :
        y = y + C[a]

print(x, y)