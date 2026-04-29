def sol(n, start, end, mid):
    if n == 0: return
    sol(n-1, start, mid, end)
    print(start, end)
    sol(n-1, mid, end, start)

n = int(input())

print(2**n - 1)
sol(n, '1', '3', '2')
