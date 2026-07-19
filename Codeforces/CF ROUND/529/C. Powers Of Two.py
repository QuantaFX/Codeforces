from collections import Counter

n, k = map(int, input().split())

bits = []
for i in range(31):
    if (n >> i) & 1:
        bits.append(1 << i)

if k < len(bits) or  k > n:
    print("NO")
else:
    print("YES")

    nums = Counter(bits)
    count = len(bits)

    for i in range(30, 0, -1):
        pow = 1 << i
        while nums[pow] > 0 and count < k:
            nums[pow] -= 1
            nums[pow//2] += 2
            count += 1

    for n, p in nums.items():
        for i in range(p):
            print(n, end=" ")