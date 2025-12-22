import sys
input = sys.stdin.read

def sol():
    data = input().split()
    ptr = 0
    t = int(data[ptr])
    ptr += 1
    results = []

    for _ in range(t):
        n = int(data[ptr])
        ptr += 1

        counts = {}
        for i in range(n):
            val = int(data[ptr])
            ptr += 1
            counts[val] = counts.get(val, 0) + 1

        ans = 0
        for val in counts:
            c = counts[val]
            ans += (c * (c - 1)) // 2

        if 1 in counts and 2 in counts:
            ans += counts[1] * counts[2]

        results.append(str(ans))
    sys.stdout.write("\n".join(results) + "\n")

sol()