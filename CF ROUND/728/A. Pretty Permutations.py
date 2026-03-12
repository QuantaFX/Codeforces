def sol():
    n = int(input())

    if n%2 == 0:
        for i in range(1, n+1):
            if i%2 == 0:
                print(i-1, end=" ")
            else:
                print(i+1, end=" ")
        print()
    else:
        for i in range(1, n-2):
            if i%2 == 0:
                print(i-1, end=" ")
            else:
                print(i+1, end=" ")

        print(n, end=" ")
        for i in range(n-2, n):
            print(i, end=" ")
        print()

tc = int(input())
while tc:
    tc -=1
    sol()