def sol():
    n = int(input())
    a = list(map(int, input().split()))

    six = []
    two = []
    three = []
    rem = []

    for i in a:
        if i % 6 == 0:
            six.append(i)
        elif i % 2 == 0:
            two.append(i)
        elif i % 3 == 0:
            three.append(i)
        else:
            rem.append(i)

    ans = six + two + rem + three
    print(*ans)

tc = int(input())
while(tc):
    sol()
    tc -= 1