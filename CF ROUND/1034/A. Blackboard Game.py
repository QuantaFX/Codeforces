def sol():
    n = int(input())
    if n % 4 == 0:
        print("Bob")
    else:
        print("Alice")

tc = int(input())
while tc:
    sol()
    tc -= 1