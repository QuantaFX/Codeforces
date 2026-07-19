def sol():
    s = input()

    if "><" in s or ">*" in s or "**" in s or "*<" in s:
        print(-1)
    else:
        l = s.count("<")
        r = s.count(">")
        if "*" in s:
            l+=1
            r+=1
        if l > r:
            print(l)
        else:
            print(r)

tc = int(input())
while tc > 0:
    tc -= 1
    sol()