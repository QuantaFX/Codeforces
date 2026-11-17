def sol():
    n = int(input())
    s = input()

    stack = []
    ans = []

    for i in range(n):
        if s[i] == '1':
            stack.append(i+1)
        elif s[i] == '2':
            if stack:
                ans.append(i+1)
                stack.pop()
    ans += stack
    ans.sort()

    print(len(ans))
    print(*ans)

tc = int(input())
while tc:
    tc -= 1
    sol()