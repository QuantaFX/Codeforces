def sol():
    str1 = input()
    str2 = input()
    str2 = ''.join(sorted(str2))

    f = False
    for i in str1:
        x = str2.find(i)
        if x != -1:
            str2 = str2[:x] + str2[x+1:]
        else:
            print("Impossible")
            f = True
            break

    if not f:
        while str2 or str1:
            if not str1:
                print(str2[0], end='')
                str2 = str2[1:]
            elif not str2:
                print(str1[0], end='')
                str1 = str1[1:]
            elif str1[0] <= str2[0]:
                print(str1[0], end='')
                str1 = str1[1:]
            else:
                print(str2[0], end='')
                str2 = str2[1:]
    print()

tc = int(input())
while tc:
    tc -= 1
    sol()