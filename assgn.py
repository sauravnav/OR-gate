# WEIGHT
# import random
# def weight():
#     w =[]
#     wt = [random.random()]
#     for i in range(2):
#         w.append(wt)
#     return w

#input-output
# def matrix(r,c):
#     m = []
#     for i in range(r):
#         row = []
#         for j in range(c):
#             x = int(input("Enter num:"))
#             row.append(x)
#         m.append(row)
#     return m
# a = int(input("Enter number of rows:"))
# b = int(input("Enter number of cols:"))

def multiply(m):

        # print(m)
a = int(input("Enter number of rows:"))
b = int(input("Enter number of columns:"))
inp_matrix(m)

# a = [[0,0],[0,1],[1,0],[1,1]]
# b = [[0.1],[0.2]]
# row1 = len((a))
# col1 = len(a[0])
# row2 = len(b)
# col2 = len(b[0])
# p = []
# for i in range(row1):
#      ai = []
#      for j in range(col2):
#          c = 0
#          ai.append(c)
#      p.append(ai)
# # print(p)
# for i in range(0,row1): # 0 4
#      for j in range(0,col2): #2
#           for k in range(0,row2):
#                p[i][j] += a[i][k] * b[k][j]
# print(p)

ACTIVATION FUNCTION:
# def sigmoid(x):
#     a = pow(2.718,x)
#     return 1/(1+a)
# DERIVATIVE OF SIGMOID FUNCTION:
# def der(x):
#     return sigmoid(x) * (1-sigmoid(x))
#INPUT-OUTPUT:
# inp = [[0,0],[0,1],[1,0],[1,1]]
# out = [[0],[1],[1],[1]]
#WEIGHT:
# import random
# w = [random.random()*2-1]
# print(w)
# for i in range(1):
#     print(w)
# w = [[0.1],[0.2]]
# for epochs in range(5):
#     input_layer = inp
#     w_sum =