sum_even_terms = 0
MAX = 4e6

first = 1
second = 2

while second <= MAX:
    if second % 2 == 0:
        sum_even_terms += second
    sumi = first + second
    first = second
    second = sumi

print(sum_even_terms)
