import math

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def sol():
    n = int(input())
    a = list(map(int, input().split()))

    prev = a[0]
    for i in range(n):
        prev = math.gcd(prev, a[i])

    if prev == 1:
        print(2)
        return

    i = 1
    while True:
        if is_prime(i):
            if prev % i != 0:
                print(i)
                return
        i +=1

tc = int(input())
while tc:
    tc -=1
    sol()