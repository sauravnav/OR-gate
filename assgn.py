# WEIGHT
# import random
# w = random.random()*2-1
# for i in range(3):
#     print(w)

#input-output
o = [0,1,1,1]
r = int(input("Enter number of rows:"))
c = int(input("Enter number of columns:"))
ai = []                    # 001 011 101 111    [[001],[011],[101],[111]]
for i in range(r):        # 0 1 2
    row =[]
    for j in range(c):   # 0 1 2
        x = int(input("Enter num:"))
        row.append(x)
    ai.append(row)
    print(ai)