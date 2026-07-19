n = int(input())

x = [input() for i in range(n)]

# Adjacent i +- 1 or j +-1
# X adjacents = 1 -> Y adjacents = 2, 3
# X adjacents >= 2 -> Y adjacents = 0, 1

for lines in x:
    print(lines)

1 2 3
2 1 4
1 3 2

1 1 1
1 2 2
2 2 2

1 4 1
4 2 3
1 1 2