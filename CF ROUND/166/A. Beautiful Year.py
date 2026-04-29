n = int(input())
i = n+1

while True:
    if len(set(str(i))) == 4:
        print(i)
        break
    i += 1