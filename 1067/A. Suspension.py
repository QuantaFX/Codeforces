def sol():
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    
tc = int(input())
while tc > 0:
    tc -= 1
    sol()