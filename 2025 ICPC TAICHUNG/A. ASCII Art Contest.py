l = list(map(int, input().split()))

l.sort()

if l[2] - l[0] >= 10:
    print("check again")
else:
    print("final", l[1])
