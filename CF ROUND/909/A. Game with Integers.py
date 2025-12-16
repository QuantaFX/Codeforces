def sol():
    n = int(input())
    if n % 3 == 0:
        print("Second")
    else:
        print("First")

tc = int(input())
while tc:
    tc -= 1
    sol()