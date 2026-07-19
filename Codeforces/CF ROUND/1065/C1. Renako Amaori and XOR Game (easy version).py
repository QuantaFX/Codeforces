def sol():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    total = sum(a) + sum(b)

    index = 0
    for i in range(n):
        if a[i] != b[i]:
            index = i

    if total%2 == 0:
        print("Tie")
    else:
        if index%2 == 0:
            print("Ajisai")
        else:
            print("Mai")

tc = int(input())
while tc:
    tc-=1
    sol()