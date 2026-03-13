n = int(input())
a = map(int, input().split())
a = sorted(a)

min_stability = sum(a)

for i in range(len(a)):
    for j in range(i+1, len(a)):

        pair = []
        for k in range(len(a)):
            if k != i and k != j:
               pair.append(a[k])

        stability = 0
        for k in range(0, len(pair), 2):
            stability += pair[k+1] - pair[k]

        if stability < min_stability:
            min_stability = stability

print(min_stability)