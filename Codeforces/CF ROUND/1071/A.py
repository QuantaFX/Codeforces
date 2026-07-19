def sol():
    s = list(input())
    n = len(s)
    c = 0

    if s[0] != 's':
        s[0] = 's'
        c+=1

    if s[-1] != 's':
        s[-1] = 's'
        c+=1

    for i in range(1, n-1):
        if s[i-1] == 's' and s[i] == 'u' and s[i+1] == 'u':
            s[i+1] = 's'
            c+=1

    print(c)

tc = int(input())
while tc:
    tc -= 1
    sol()