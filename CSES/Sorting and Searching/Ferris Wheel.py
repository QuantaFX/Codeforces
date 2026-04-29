from collections import Counter

n, x = map(int, input().split())
a = list(map(int, input().split()))

counts = Counter(a)

unique_vals = sorted(counts.keys())
left_idx = 0
right_idx = len(unique_vals) - 1

count = 0

while left_idx <= right_idx:
    left = unique_vals[left_idx]
    right = unique_vals[right_idx]

    if counts[left] == 0:
        left_idx += 1
        continue
    if counts[right] == 0:
        right_idx -= 1
        continue

    if left == right:
        if right * 2 <= x:
            count += counts[right] // 2 + counts[right] % 2
        else:
            count += counts[right]
        break
    elif left + right <= x:
        mini = min(counts[left], counts[right])
        counts[left] -= mini
        counts[right] -= mini
        count += mini
    else:
        count += counts[right]
        counts[right] = 0
        right_idx -= 1

print(count)