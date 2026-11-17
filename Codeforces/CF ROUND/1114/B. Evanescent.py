def sol():
    a = int(input())
    s = input()

    base_len = 1
    for i in range(a-1):
        if s[i] != s[i+1]:
            base_len += 1

    min_len = base_len
    for i in range(1, a-1):
        old_cost = (1 if s[i-1] != s[i]  else 0) + (1 if s[i] != s[i+1] else 0)
        new_cost = 0 if s[i-1] == s[i+1] else 1
        diff =  old_cost - new_cost
        min_len = min(min_len, base_len-diff)

    print(min_len)

tc = int(input())
while tc:
    tc -= 1
    sol()