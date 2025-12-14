def sol():
    n = int(input())
    b = list(map(int, input().split()))
    a = [0] * n
    prev_left = 0
    prev_right = float('inf')

    for i in range(n // 2):
        target_sum = b[i]
        left_val = prev_left
        right_val = target_sum - left_val
        if right_val > prev_right:
            diff = right_val - prev_right
            left_val += diff
            right_val -= diff
        a[i] = left_val
        a[n - 1 - i] = right_val
        prev_left = left_val
        prev_right = right_val
    print(*a)
sol()