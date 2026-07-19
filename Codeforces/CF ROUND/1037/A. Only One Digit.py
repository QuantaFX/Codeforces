def sol():
    n = input()
    MIN = 9
    for i in n:
        if int(i) < MIN:
            MIN = int(i)
    print(MIN)

tc = int(input())
while tc:
    sol()
    tc -= 1