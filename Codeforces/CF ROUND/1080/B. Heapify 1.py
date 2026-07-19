def odd_chain(num):
    while num % 2 == 0:
        num //= 2
    return num

def sol():
    n = int(input())
    a = list(map(int, input().split()))

    a = [0] + a
    for i in range(1, n+1):
        if odd_chain(a[i]) != odd_chain(i):
            print("NO")
            return

    print("YES")

tc = int(input())
while tc:
    tc -= 1
    sol()