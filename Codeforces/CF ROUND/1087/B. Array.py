lines = int(input())
Letters = ""
for i in range(lines):
    ins = input().split()
    if ins[0] == "I":
        ind = int(ins[1])
        reps = int(ins[2])
        char = ins[3]
        Letters = Letters[:ind] + (char * reps) + Letters[ind:]
    else:
        print(Letters[int(ins[1])])