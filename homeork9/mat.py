import random
class Matrix:
   count=0
   def __init__(self,rows,cols):
    Matrix.count+=1
    self.mat=[]
    self.rows=rows
    self.cols=cols
    for i in range(0,rows):
      a=[]
      for j in range(0,cols):
        a.append(random.randint(1,10))
      self.mat.append(a)

   def printMat(self,name):
      print("\nMatrix",name,": ")
      column_width = 3
      for row in self.mat:
        print(" ".join(f"{element:>{column_width}}" for element in row))

   def __str__(self):
      return f"\nRows: {self.rows}, Columns: {self.cols},\nMatrix: {self.mat}"
      
   def checkDimensions(self,other):
      return(self.rows==other.rows and self.cols==other.cols)
    
   def __add__(self,other):
      if not self.checkDimensions(other):
            raise ValueError("Matrices must have the same dimensions.")
      result = Matrix(self.rows, self.cols)
      result.mat = [
            [self.mat[i][j] + other.mat[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
      return result

   def __sub__(self,other):
       if not self.checkDimensions(other):
            raise ValueError("Matrices must have the same dimensions.")  
       result=Matrix(self.rows,self.cols)
       result.mat=[
          [self.mat[i][j]-other.mat[i][j] for j in range(self.cols)]
          for i in range(self.rows)
       ]
       return result
   
   def __mul__(self,other):
      if self.cols != other.rows:
        raise ValueError("Number of columns in the first matrix must equal the number of rows in the second matrix.")
      result = Matrix(self.rows, other.cols)
      result.mat = [
        [
            sum(self.mat[i][k] * other.mat[k][j] for k in range(self.cols))
            for j in range(other.cols)
        ]
        for i in range(self.rows)
      ]
      return result 

m1=Matrix(4,5)
m1.printMat("1")
print("\nstr() string1:",m1.__str__())

m2=Matrix(4,5)
m2.printMat("2")
print("\nstr() string2:",m2.__str__())

addM=m1+m2
addM.printMat("Addition for matrix1 and matrix2:")

subM=m1-m2
subM.printMat("Subtraction for matrix1 and matrix2:")


m3=Matrix(4,5)
m3.printMat("3")

m4=Matrix(5,4)
m4.printMat("4")


mulM=m3*m4
mulM.printMat("Multiplication for matrix3 and matrix4:")
