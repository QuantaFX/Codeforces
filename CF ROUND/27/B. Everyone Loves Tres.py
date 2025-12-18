def sol():
    n = int(input())

    if n == 1 or n == 3:
        print(-1, end="")
    elif n % 2 == 0:
        for i in range(n):
            if i < n-2:
                print(3, end="")
            else:
                print(6, end="")
    else:
        for i in range(n):
            if i < n-4 or i == n-3:
                print(3, end="")
            else:
                print(6, end="")
    print()

tc = int(input())
while tc:
    tc -= 1
    sol()