def sol():
    a, b, n = map(int, input().split())

    if a == b or b*n <= a:
        print("1")
    else:
        print("2")
tc = int(input())
while tc:
    sol()
    tc -= 1