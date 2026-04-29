def sol():
    n, m, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print(n+m)

tc = int(input())
while tc:
    tc-=1
    sol()