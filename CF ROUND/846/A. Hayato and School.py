def sol():
    n = int(input())
    s = list(map(int, input().split()))

    odd = []
    even = []

    for i in range(n):
        if s[i] % 2 == 0:
            even.append(i+1)
        else:
            odd.append(i+1)

    if len(odd) >= 3:
        print("YES")
        ans = odd[0:3]
        print(*ans)
    elif len(odd) >= 1 and len(even) >= 2:
        print("YES")
        ans = even[0:2]
        ans.append(odd[0])
        print(*ans)
    else:
        print("NO")



tc = int(input())
while tc:
    tc -= 1
    sol()