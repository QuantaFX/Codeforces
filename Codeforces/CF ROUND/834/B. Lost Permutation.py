def sol():
    m, s = map(int, input().split())
    l = list(map(int, input().split()))

    maxi = max(l)
    added = 0

    i = 1
    while added < s or i <= maxi:
        if i not in l:
            added += i
        i+=1


    if added == s and i >= maxi:
        print("YES")
    else:
        print("NO")


tc = int(input())
while tc:
    tc -= 1
    sol()