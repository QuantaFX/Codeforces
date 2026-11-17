def sol():
    n = int(input())
    a = list(map(int, input().split()))

    odd_cnt, div_four_cnt, non_div_four_cnt = 0, 0, 0

    for num in a:
        if num % 2 == 1:
            odd_cnt += 1
        elif num % 4 == 0:
            div_four_cnt += 1
        else:
            non_div_four_cnt += 1

    print(max(odd_cnt, div_four_cnt, non_div_four_cnt))

tc = int(input())
while tc:
    tc -= 1
    sol()