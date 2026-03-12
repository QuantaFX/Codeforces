def sol():
    n = int(input())
    s = list(map(int, input().split()))

    zero = s.count(0)

    if zero > 0:
        if s[0] == 1 or s[-1] == 1:
            print("Alice")
        else:
            print("Bob")
    else:
        print("Alice")

tc = int(input())
while tc:
    sol()
    tc -= 1