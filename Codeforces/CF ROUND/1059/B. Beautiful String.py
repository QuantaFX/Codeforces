def palindrome(s):
    return s == s[::-1]

def increasing(s):
    if not s: return True
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            return False
    return True

def sol():
    n = int(input())
    s = input()

    for mask in range(1 << n):
        p_indices = []
        p_chars = []
        x_chars = []

        for i in range(n):
            if (mask >> i) & 1:
                p_indices.append(i)
                p_chars.append(s[i])
            else:
                x_chars.append(s[i])

        if increasing("".join(p_chars)) and palindrome("".join(x_chars)):
            print(len(p_indices))
            print(*(i + 1 for i in p_indices))
            return

    print("-1")

tc = int(input())
while tc:
    sol()
    tc -= 1