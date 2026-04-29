n = int(input())
MOD = 10**9 + 7
num = 1
for i in range(1, n+1):
    num = (num * 2) % MOD
print(num)