def sol():
    n = int(input())
    a = list(map(int, input().split()))

    run_sum, minimum_required = 0, 0
    for i in range(n):
        minimum_required += i+1
        run_sum += a[i]

        if run_sum < minimum_required:
            print("NO")
            return
    
    print("YES")

tc = int(input())
while tc:
    tc -= 1
    sol()