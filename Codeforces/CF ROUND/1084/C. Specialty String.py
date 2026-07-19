def sol():
    n = int(input())
    s = input()

    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    if stack:
        print("NO")
    else:
        print("YES")

tc = int(input())
while tc:
    tc -= 1
    sol()