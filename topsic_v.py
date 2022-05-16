#りんごとみかんの箱詰め

N = int(input())
S = input()

a = ""
b = 0

for x in S:
    if a != x:
        b = b + 1
        a = x
        
print(b)