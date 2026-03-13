def sol():
    n = int(input())
    a = input()

    total_a = a.count('a')
    total_b = a.count('b')

    cost_a = 0
    cost_b = 0
    a_count = 0
    b_count = 0

    for char in a:
        if char == 'a':
            a_count += 1
            b_right = total_b - b_count
            cost_b += min(b_count, b_right)
        else:
            b_count += 1
            a_right = total_a - a_count
            cost_a += min(a_count, a_right)

    print(min(cost_a, cost_b))

tc = int(input())
while tc:
    tc -= 1
    sol()