def sol():
    s1 = str(input())
    s2 = input()

    s1 = sorted(s1)
    if s2 != "abc" or "b" not in s1 or "c" not in s1 or "a" not in s1:
        print("".join(s1))
    else:
        print("a" * s1.count('a') + "c" * s1.count('c') + "b" * s1.count('b'), end="")
        for i in s1:
            if i > "c":
                print(i, end="")
        print()
tc = int(input())
while tc:
    tc -= 1
    sol()