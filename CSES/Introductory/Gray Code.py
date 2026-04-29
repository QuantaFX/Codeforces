n = int(input())

for i in range(1 << n):
    g = i ^ (i >> 1)
    s = ""
    for j in range(n-1, -1, -1):
        if g & (1 << j):
            s += "1"
        else:
            s += "0"
    print(s)