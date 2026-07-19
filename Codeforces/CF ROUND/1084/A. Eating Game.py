def sol():
    n = int(input())
    s = list(map(int, input().split()))
    print(s.count(max(s)))

tc = int(input())
while tc:
    tc -= 1
    sol()