def minput(r,c,matrix):
    print("Enter the numbers row wise: ")
    for i in range(r):
        a = []
        for j in range(c):
            b = int(input())
            a.append(b)
    matrix.append(a)

def moutput(matrix):
    for i in range(3):
        for j in range(3):
            print(matrix[i][j], end =" ")
            print()

def add(r1,c1,matrix1,matrix2):
    d = []
    for i in range(r1):
        c = []
        for j in range(c1):
            c.append(matrix1[i][j] + matrix2[i][j])
        d.append(c)
    print("Addition of two matrices: ")
    moutput(d)

def sub(r1,c1,matrix1,matrix2):
    d = []
    for i in range(r1):
        c = []
        for j in range(c1):
            c.append(matrix1[i][j] - matrix2[i][j])
        d.append(c)
    print("Substraction of two matrices: ")
    moutput(d)

def transpose(r1,c1,matrix1):
    e = []
    for i in range(r1):
        f = []
        for j in range(c1):
            f.append(matrix1[j][i])
        e.append(f)
    print("Transpose of matrix is: ")
    moutput(e)
    return e

def mult(matrix1,matrix2,r1,c2):
    matrix3 = []
    for i in range(r1):
        z = []
        for j in range(c2):
            g = 0
            for k in range(r1):
                g = g + (matrix1[i][k] + matrix2[k][j])
            z.append(g)
        matrix3.append(z)
    print("Multiplication of two matrices: ")
    moutput(matrix3)

r1 = int(input("Enter the number of rows of matrix 1: "))
c1 = int(input("Enter the number of columns of matrix 1: "))
matrix1 = []
minput(r1,c1,matrix1)


r2 = int(input("Enter the number of rows of matrix 2: "))
c2 = int(input("Enter the number of columns of matrix 2: "))
matrix2 = []
minput(r2,c2,matrix2)

print("Matrix 1 is: ")
moutput(matrix1)

print("Matrix 2 is: ")
moutput(matrix2)

add(r1,c1,matrix1,matrix2)
sub(r1,c1,matrix1,matrix2)
transpose(r1,c1,matrix1)
mult(matrix1,matrix2,r1,c2)

