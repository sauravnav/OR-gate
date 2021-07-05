# OR-gate
def creatematrix (rowno,colno):
 matrix = []
 for j in range(rowno) :         #limiting the value from start to the rowno
  row =[ ]
  for k in range(colno):
    x = int(input("Enter the number"))     #entering the value inside matrix
    row.append(x)
  matrix.append(row)
 global matrix
 print(matrix)
m = int(input("Enter the rowno"))
n = int(input("Enter the colno"))
creatematrix(m,n)

def input( ):                            #selecting 2 inputs for or gate
    r = 1;
    mat = []
    weight = ([0.1],[0.2])               #random weight assignment
    for r in range(m):
      in1 = matrix(r,1)
      in2 = matrix(r,2)
      z = (in1*weight(1))+(in2*weight(2))   #only considered 2 inputs ,no bias
      mat.append(z)                        #not neccessary , just for storing
