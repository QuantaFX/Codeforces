def sol():
    n = int(input())
    a = list(map(int, input().split()))

    count_map = {}
    for i in a:
        count_map[i] = count_map.get(i, 0) + 1

    count = {}
    idx = 1
    for k, v in count_map.items():
        if v % k != 0:
            print(-1)
            return
        count[k] = [idx, k]
        idx += (v//k)

    ans = []
    for num in a:
        ans.append(count[num][0])
        count[num][1] -= 1
        if count[num][1] == 0:
            count[num][0] += 1
            count[num][1] = num
    print(*ans)

tc = int(input())
while tc:
    tc -= 1
    sol()