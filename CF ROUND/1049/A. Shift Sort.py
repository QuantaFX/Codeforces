def sol():
    n = int(input())
    s = input()

    c = s.count('0')
    s = s[:c]
    print(s.count('1'))

tc = int(input())
while tc:
    tc -= 1
    sol()