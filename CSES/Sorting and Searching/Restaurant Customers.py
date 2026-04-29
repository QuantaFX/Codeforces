import sys

input_data = sys.stdin.read().split()
data = list(map(int, input_data))

arrivals = data[1::2]
departures = data[2::2]

arrivals.sort()
departures.sort()

n = data[0]
max_customers, current_customers = 0, 0
i, j = 0, 0

while i < n:
    if arrivals[i] < departures[j]:
        current_customers += 1
        if current_customers > max_customers:
            max_customers = current_customers
        i += 1
    else:
        current_customers -= 1
        j += 1

print(max_customers)
