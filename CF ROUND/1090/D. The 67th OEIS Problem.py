def sieve(n):
    prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    res = []
    for p in range(2, n + 1):
        if prime[p]:
            res.append(p)

    return res

MAX = 10**6
primes = sieve(MAX)

def sol():
    n = int(input())
    for i in range(n):
        print(primes[i]*primes[i+1], end=" ")
    print()

tc = int(input())
while tc:
    sol()
    tc -= 1