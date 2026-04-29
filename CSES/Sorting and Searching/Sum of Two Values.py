n, x = map(int, input().split())
a = list(map(int, input().split()))

arr = [(val, i+1) for i, val in enumerate(a)]
arr.sort()

def sol():
    left = 0
    right = n-1
    while left < right:
        current_sum = arr[left][0] + arr[right][0]
        if current_sum == x:
            print(arr[left][1], arr[right][1])
            return
        elif current_sum < x:
            left += 1
        else:
            right -= 1
    print("IMPOSSIBLE")

sol()