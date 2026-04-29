n, q = map(int, input().split())
a = list(map(int, input().split()))

sumi = [0] * (n+1)

summation = 0
for i in range(len(a)):
    summation += a[i]
    sumi[i+1] = summation

for i in range(q):
    a, b = map(int, input().split())
    print(sumi[b]-sumi[a-1])
