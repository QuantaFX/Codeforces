def sol():
    a, b, c = map(int, input().split())
    curr_dif = abs(a-b)
    if a >= b:
        ans = a + c - b
    else:
        if abs(a+c - b) > curr_dif:
            ans = abs(a+c - b)
        else:
            ans = curr_dif
    print(ans)

tc = int(input())
while tc:
    tc -= 1
    sol()