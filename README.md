# OR-gate
def creatematrix (rowno,colno):
 matrix = []
 for j in range(rowno) :         #limiting the value from start to the rowno
  row =[ ]
  for k in range(colno):
    x = int(input("Enter the number"))     #entering the value inside matrix
    row.append(x)
  matrix.append(row)

 print(matrix)
m = int(input("Enter the rowno"))
n = int(input("Enter the colno"))
creatematrix(m,n)
