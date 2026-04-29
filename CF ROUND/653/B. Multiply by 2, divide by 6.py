def sol():
    n = int(input())
    moves = 0
    while n > 1:
        if n % 6 == 0:
            n //= 6
            moves += 1
        elif n % 3 == 0:
            n *= 2
            moves += 1
        else:
            print(-1)
            return
    print(moves)

tc = int(input())
while tc:
    tc -= 1
    sol()