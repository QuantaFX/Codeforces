def sol():
    n, m = map(int, input().split())

    if n == 1 and m == 1:
        print(0)
    elif min(n, m) == 1:
        print(1)
    else:
        print(2)
tc = int(input())
while tc:
    tc-=1
    sol()