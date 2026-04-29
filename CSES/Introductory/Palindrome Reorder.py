n = input()
letter = [0 for i in range(26)]
for i in n:
    letter[ord(i)-65] += 1
arr = []
mid = []
count = 0
for i in range(26):
    if letter[i]%2 != 0:
        for j in range(letter[i]):
            mid.append(chr(i+65))
        count += 1
    else:
        for j in range(letter[i]//2):
            arr.append(chr(i+65))

if count > 1:
    print("NO SOLUTION")
else:
    for i in arr:
        print(i, end="")
    for i in mid:
        print(i, end="")
    for i in arr[::-1]:
        print(i, end="")
