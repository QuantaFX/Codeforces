def sol():
    n = int(input())
    s = input()

    current_count, max_count = 0, 0
    for i in range(n):
        if s[i] == '#':
            current_count += 1
        else:
            current_count = 0
        max_count = max(max_count, current_count)

    if max_count%2 == 0:
        print(max_count//2)
    else:
        print(max_count//2 + 1)

tc = int(input())
while tc:
    tc -= 1
    sol()