n = int(input())
arr = list(map(int, input().split()))

pos_pre = 1
neg_pre = 0
sign = 1
pos_sub = 0
neg_sub = 0

for i in range(n):
    if arr[i] < 0:
        sign *= -1
    if sign == 1:
        pos_sub += pos_pre
        neg_sub += neg_pre
        pos_pre += 1
    else:
        pos_sub += neg_pre
        neg_sub += pos_pre
        neg_pre += 1

print(neg_sub, pos_sub)