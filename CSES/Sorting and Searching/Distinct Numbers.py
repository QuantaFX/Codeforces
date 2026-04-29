import sys
inp = sys.stdin.read
data = inp().split()
print(len(set(data[1:])))