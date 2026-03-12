def sol():
    n = int(input())
    s = input()

    if "2025" not in s or "2026" in s:
        print(0)
    else:
        print(1)

tc = int(input())
while tc:
    tc -=1
    sol()