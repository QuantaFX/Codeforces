def sol():
    n, a, b = map(int, input().split())
    j = 0

    for i in range(n):
        print(chr(ord('a') + j), end="")
        j = 0 if (i+1) % a == 0 else (j+1)%b

tc = int(input())
while tc:
    tc -= 1
    sol()
    print()