# A = 1-9                 1 * 9
# B = 9*10-9*90 + 9*A     2 * 90
# C = 9*100-9*900 + 9*B   3 * 900
# D = 9*1000-9*9000 + 9*C 4 * 900

def len_digits(x):
    s = str(x)
    n = len(s)
    total = 0
    for i in range(1, n):
        total += 9*(10**(i-1)) * i
    total += (x-10**(n-1)+1) * n
    return total

def sum_digits(x):
    s = str(x)
    n = len(s)

    dp = {}
    def solve(idx, less, curr):
        state = (idx, less)

        if state in dp:
            return dp[state]
        if idx == len(curr):
            return 0, 1

        lim = int(curr[idx]) if not less else 9
        sum, count = 0, 0

        for d in range(lim+1):
            n_less = less or (d<lim)
            s_val, c_val = solve(idx+1, n_less, curr)
            sum += s_val + d * c_val
            count += c_val

        dp[state] = (sum, count)
        return sum, count

    sum, _ = solve(0, False, s)
    return sum

def sol():
    k = int(input())

    min, max, N = 1,  10**15, 10**15
    while min <= max:
        mid = (min+max) // 2
        if len_digits(mid) >= k:
            N = mid
            max = mid-1
        else:
            min = mid+1

    total_sum = sum_digits(N)
    extra_count = len_digits(N) - k
    s = str(N)
    for i in range(extra_count):
        total_sum -= int(s[-(i + 1)])
    print(total_sum)

tc = int(input())
while tc:
    tc-=1
    sol()