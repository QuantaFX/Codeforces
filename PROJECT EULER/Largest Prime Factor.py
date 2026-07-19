n = 600851475143

largestPrime = -1

while n % 2 == 0:
    largestPrime = 2
    n //= 2

i = 3
while i * i <= n:
    while n % i == 0:
        largestPrime = i
        n //= i
    i += 2

if n > 2:
    largestPrime = n

print(largestPrime)