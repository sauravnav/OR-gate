# WEIGHT
# import random
# w = [random.random()*2-1]
# for i in range(2):
#     print(w)

#input-output
# def matrix(r,c):
#     m = []
#     for i in range(r):
#         row = []
#         for j in range(c):
#             x = int(input("Enter num:"))
#             row.append(x)
#         m.append(row)
#         print(m)
# a = int(input("Enter number of rows:"))
# b = int(input("Enter number of columns:"))
# matrix(a,b)

# a = pow(2.718,5)
# s = 1 /(1+a)
# print(s)

a = [[0,0],[0,1],[1,0],[1,1]]
b = [[0.1],[0.2]]
row1 = len((a)) 
col1 = len(a[0])
row2 = len(b)
col2 = len(b[0])
p = []
for i in range(row1):
     ai = []
     for j in range(col2):
         c = 0
         ai.append(c)
     p.append(ai)
# print(p)
for i in range(0,row1): # 0 4
     for j in range(0,col2): #2
          for k in range(0,row2):
               p[i][j] += a[i][k] * b[k][j]
print(p)