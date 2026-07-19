def sol():
    n = int(input())
    s = list(map(int, input().split()))

    mini = 2 * s[0] -1
    total = 0

    for i in range(1, n):
        total += (s[i]-1) // mini

    print(total)
tc = int(input())
while tc:
    tc -= 1
    sol()