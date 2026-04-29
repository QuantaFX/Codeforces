def sol():
    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    v = input()

    s.sort()

    # RUNNING SUM OF VOTES
    run_sum = [0] * (n+1)
    sumi = 0
    for i in range(n):
        if v[i] == '1':
            sumi += 1
        run_sum[i+1] = sumi

    # MAXIMUM SUBSETS
    maxi = 2**m

    # SUM OF TURNED ON BITS
    pos = [0] * maxi
    for i in range(1, maxi):
        # FAST LSB
        lsb = i & -i
        barrio = lsb.bit_length()-1
        # RATHER THAN CHECK THE REST JUST CHECK THE LSB AND
        # ADD THAT TO AN EXISTING ONE (BEFORE IT)
        pos[i] = pos[i^lsb] + s[barrio]

    print(*pos)

    dp = [0] + [-1] * (maxi-1)
    for mask in range(maxi):
        # CANT REACH THIS SUBSET
        if dp[mask] == -1: continue

        cur_pos = pos[mask]
        for i in range(m):
            # IF NOT ON (USED) & (First / No copy /
            if not (mask & (1 << i)) and (i == 0 or s[i] != s[i-1] or (mask & (1<<(i-1)))):

                # IF THE AMOUNT OF VOTES IN (POS -> POS + SIZE) > HALF (MAJORITY)
                win = 0
                if run_sum[cur_pos+s[i]] - run_sum[cur_pos] > s[i] // 2:
                    win = 1

                # UPDATE MAX WINS IN THAT COUNT
                nxt_mask = mask | (1<<i)
                if dp[mask] + win > dp[nxt_mask]:
                    dp[nxt_mask] = dp[mask] + win

    print(dp[maxi-1])

tc = int(input())
while tc:
    tc-=1
    sol()