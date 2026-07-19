def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

def check():
    maxi = 0
    for i in range(999,-1,-1):
        for j in range(999,-1,-1):
            if is_palindrome(i*j):
                print(i*j, i, j)
                maxi = max(maxi, i*j)
    return maxi

print(check())