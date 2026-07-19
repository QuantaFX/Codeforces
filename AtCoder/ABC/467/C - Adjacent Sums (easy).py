n, m = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

Ab = [0] * n
Ab[0] = 1
Ac = [0] * n

for i in range(n-1):
    if B[i] != (Ab[i] + Ab[i+1]) % 2:
        Ab[i+1] = (Ab[i+1]+1)%2

    if B[i] != (Ac[i] + Ac[i+1]) % 2:
        Ac[i+1] = (Ac[i+1]+1)%2

changes_a, changes_b = 0, 0
for i in range(n):
    if Ab[i] != A[i]:
        changes_a += 1
    if Ac[i] != A[i]:
        changes_b += 1

print(min(changes_a, changes_b))
