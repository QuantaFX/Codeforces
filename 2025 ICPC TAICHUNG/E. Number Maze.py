from itertools import permutations

def sol():
    s, a, b = map(int, input().split())
    s = str(s)

    r = ["".join(p) for p in permutations(s)]

    a = r[a-1]
    b = r[b-1]

    A = 0
    B = 0
    for i in range(len(s)):
        if a[i] == b[i]:
            A += 1
        elif a[i] in b:
            B += 1

    print(str(A)+"A"+str(B)+"B")

tc = int(input())
while tc > 0:
    tc -= 1
    sol()