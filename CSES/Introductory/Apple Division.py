n = int(input())
a = list(map(int, input().split()))

def find_min_difference(arr, n, sum_calculated, sum_total):
    if n == 0: return abs((sum_total - sum_calculated) - sum_calculated)
    include = find_min_difference(arr, n - 1, sum_calculated + arr[n - 1], sum_total)
    exclude = find_min_difference(arr, n - 1, sum_calculated, sum_total)
    return min(include, exclude)

def min_difference(arr):
    sum_total = 0
    for num in arr: sum_total += num
    return find_min_difference(arr, len(arr), 0, sum_total)

print(min_difference(a))