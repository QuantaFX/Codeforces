def sol():
    s = input()

    check = "abc"

    diff = 0
    for i in range(3):
        if s[i] != check[i]:
            diff += 1

    if diff == 3:
        print("NO")
    else:
        print("YES")

tc = int(input())
while tc:
    tc -=1
    sol()