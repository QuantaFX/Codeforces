import random
import string


def solve_needle(s, t):
    # Core logic from your provided solution
    t_sorted = sorted(list(t))
    s_list = list(s)

    # Check if s can be a subsequence of t
    remaining_t = t_sorted[:]
    for char in s_list:
        if char in remaining_t:
            remaining_t.remove(char)
        else:
            return "Impossible"

    # Lexicographical Merge
    res = []
    i, j = 0, 0
    t_rem = remaining_t
    while i < len(s_list) or j < len(t_rem):
        if i == len(s_list):
            res.append(t_rem[j])
            j += 1
        elif j == len(t_rem):
            res.append(s_list[i])
            i += 1
        elif s_list[i] <= t_rem[j]:
            res.append(s_list[i])
            i += 1
        else:
            res.append(t_rem[j])
            j += 1
    return "".join(res)


def generate_needle_suite():
    test_cases = []

    # 1. Basic Samples & Edge Cases
    test_cases.append(("abc", "abccba"))  # s is half of t
    test_cases.append(("apple", "apple"))  # s is t
    test_cases.append(("xyz", "abc"))  # Impossible

    # 2. Lexicographical Tie-Breakers
    # Tests if 'a' from s is placed before 'b' from t
    test_cases.append(("banana", "aaannnbbb"))

    # 3. Small Random cases
    for _ in range(10):
        s_len = random.randint(3, 8)
        s = "".join(random.choices(string.ascii_lowercase, k=s_len))
        # Ensure t contains s plus some extras
        t = s + "".join(random.choices(string.ascii_lowercase, k=random.randint(2, 5)))
        test_cases.append((s, t))

    # 4. Large Scale Subtask (Total |t| <= 10^5)
    n_large = 50000
    s_large = "m" * (n_large // 2)
    t_large = s_large + "a" * (n_large // 4) + "z" * (n_large // 4)
    test_cases.append((s_large, t_large))

    # Write input.txt and answer.txt
    with open("input.txt", "w") as f_in, open("answer.txt", "w") as f_out:
        f_in.write(f"{len(test_cases)}\n")
        for s, t in test_cases:
            # Shuffle t so it's not already sorted
            t_shuffled = list(t)
            random.shuffle(t_shuffled)
            t_str = "".join(t_shuffled)

            f_in.write(f"{s}\n{t_str}\n")
            f_out.write(f"{solve_needle(s, t_str)}\n")


if __name__ == "__main__":
    generate_needle_suite()
    print("Test suite generated: input.txt and answer.txt")