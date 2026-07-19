N = int(input())

lost_change = 0
for _ in range(N):
    A, B, S = map(str, input().split())
    A, B  = int(A), int(B)

    if S == "keep":
        lost_change += B-A

print(lost_change)
