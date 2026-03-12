def sol():
    a, b, c = map(int, input().split())

    total = a + b + c

    if total//3 == total/3 and total/3  >= max(a, b):
        print("YES")
    else:
        print("NO")

tc = int(input())
while tc:
    tc -=1
    sol()