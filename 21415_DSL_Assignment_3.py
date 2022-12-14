# Name - Vedant Kokane
# Roll no - 21415

class Matrix:

    def __init__(self,r,c):
        self.r = r
        self.c = c


    # Function for finding length
    def length(self, x):
        length = 0
        for i in x:
            length = length + 1
        return length

    # Function for Input of Matrix
    def matrix_input(self):
        matrix_1 = []
        r = self.r
        c = self.c
        for i in range(r):
            row = []
            for j in range(c):
                n = int(input(f" Enter number for row {i + 1},{j + 1} : "))
                row.append(n)
            matrix_1.append(row)
        return matrix_1

    # Function for Matrix Printing
    def print_matrix(self,matrix):
        r = self.length(matrix)
        for j in range(r):
            print(matrix[j])


    # Function for Matrix addition
    def add_matrix(self,matrix_1,matrix_2):
        result = []
        r = self.length(matrix_1)
        c = self.length(matrix_1[0])
        for i in range(r):
            row = []
            for j in range(c):
               sum = matrix_1[i][j] + matrix_2[i][j]
               row.append(sum)
            result.append(row)
        return result

    # Function for Matrix subtraction
    def sub_matrix(self,matrix_1,matrix_2):
        result = []
        r = self.length(matrix_1)
        c = self.length(matrix_1[0])
        for i in range(r):
            row = []
            for j in range(c):
                difference = matrix_1[i][j] - matrix_2[i][j]
                row.append(difference)
            result.append(row)
        return result

    # Function for Transpose of an Matrix
    def transpose(self,matrix_1):
        mat = []
        r = self.length(matrix_1)
        c = self.length(matrix_1[0])
        for i in range(r):
            row = []
            for j in range(c):
                r = matrix_1[j][i]
                row.append(r)
            mat.append(row)
        return mat

    # Function for Multiplication of Matrix
    def multiplication(self,mat1,mat2):
        result= []
        matrix_1_row = self.length(mat1)
        matrix_2_column  = self.length(mat2[0])
        matrix_2_row = self.length(mat2)
        for i in range(matrix_1_row):
            row = []
            for j in range(matrix_2_column):
                sum = 0
                for k in range(matrix_2_row):
                    sum = sum + mat1[i][k] * mat2[k][j]
                row.append(sum)
            result.append(row)
        return result

r1 = int(input("Please enter the number of rows for matrix 1 : "))
c1 = int(input("Please enter the number of columns for matrix 1 : "))
x = Matrix(r1,c1)
matrix_1 = x.matrix_input()
x.print_matrix(matrix_1)
r2 = int(input("Please enter the number of rows for matrix 2 : "))
c2 = int(input("Please enter the number of columns for matrix 2 : "))
x = Matrix(r2,c2)
matrix_2 = x.matrix_input()
x.print_matrix(matrix_2)

choice = "y"

while choice != "n":
    print("=" * 90)
    print("1. Matrix Addition ")
    print("2. Matrix Subtraction")
    print('3. Multiplication of 2 Matrices')
    print("4. Matrix Transpose")
    print("=" * 90)
    c = int(input("Please type the operation to be performed : "))

    if c==1:
        if r1==r2 and c1==c2:
            add = x.add_matrix(matrix_1,matrix_2)
            print("Addition of 2 given matrices is ")
            x.print_matrix(add)
        else:
            print("The number of rows and number of columns are not equal so operation not possible.")
    elif c==2:
        if r1 == r2 and c1 == c2:
            sub = x.sub_matrix(matrix_1, matrix_2)
            print("Subtraction of 2 given matrices is ")
            x.print_matrix(sub)
        else:
            print("The number of rows and number of columns are not equal so operation not possible.")
    elif c==3:
        if r1==c2 and r2==c1:
            mul = x.multiplication(matrix_1,matrix_2)
            print("Multiplication of 2 given matrices is ")
            x.print_matrix(mul)
        else:
            print("Operation not possible.")
    elif c==4:
        ask = int(input("Type for which matrix (1 or 2) transpose operation to be performed "))
        if ask == 1:
            transpose = x.transpose(matrix_1)
            print("Transpose of Matrix 1 is ")
            x.print_matrix(transpose)
        elif ask==2:
            transpose = x.transpose(matrix_2)
            print("Transpose of Matrix 2 is ")
            x.print_matrix(transpose)
        else:
            print("You have selected a matrix which does not exist.")
    else:
        print("You have selected a wrong choice.")

    print("Do you want to try any other operation ? (y/n)")
    choice = input("")

