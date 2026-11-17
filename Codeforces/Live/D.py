from collections import Counter

def sol():
    n = int(input())
    a = list(map(int, input().split()))
    count = Counter(a)

    if count[0] == 0:
        print("YES")
        print("A"*n)
        return

    if count[0] == 1:
        print("NO")
        return

    max_3_count = 0
    while count[max_3_count] > 2: max_3_count += 1

    max_2_count = 0
    while count[max_2_count] > 1: max_2_count += 1

    ans, added = [], {}

    for i in range(n):
        count = added[a[i]] = added.get(a[i], 0) + 1

        if max_3_count > a[i]:
            if count == 1:
                ans.append("A")
            elif count == 2:
                ans.append("B")
            else:
                ans.append("C")
        elif max_2_count > a[i]:
            if count == 1:
                ans.append("B")
            else:
                ans.append("C")
        elif max_3_count + max_2_count > a[i]:
            ans.append("C")
        else:
            ans.append("A")

    print("YES")
    print("".join(ans))

tc = int(input())
while tc:
    tc -= 1
    sol()