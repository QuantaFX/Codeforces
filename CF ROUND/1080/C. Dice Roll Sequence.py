def sol():
    n = int(input())
    a = list(map(int, input().split()))

    count = 0
    counting = 1
    for i in range(n-1):

        if a[i] == a[i+1] or 7-a[i] == a[i+1]:
            counting += 1
        else:
            count += int(counting/2)
            counting = 1

    count += int(counting / 2)
    print(count)

tc = int(input())
while tc:
    tc -= 1
    sol()