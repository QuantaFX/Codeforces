n = int(input())

if n%4 == 0 or n%4 == 3:
    print("YES")

    half = n * (n + 1) // 4
    first = []
    second = []

    if n%2 == 1:
        first.append(n)
        half -= n
        n -= 1

    for i in range(1, half//n + 1):
        first.append(i)
        first.append(n - i + 1)
    for i in range(half//n + 1, n//2 + 1):
        second.append(i)
        second.append(n - i + 1)

    print(len(first))
    print(*first)
    print(len(second))
    print(*second)
else:
    print("NO")