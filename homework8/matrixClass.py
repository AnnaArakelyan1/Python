import random
class Matrix:
    def __init__(self,n,m):
        self.n=n
        self.m=m
        self.mat=[]
        for i in range(n):
          a=[]
          for j in range(m):
            a.append(random.randint(1,100))
            # a.append(int(input("Enter an element: ")))
          self.mat.append(a)
    
    def printMat(self):
        for i in range(self.n):
          for j in range(self.m):
              print(self.mat[i][j],end = "  ")
          print("")
          
    def getMatMean(self):
        Sum=0
        for i in range(self.n):
          Sum += sum(self.mat[i])
        return Sum/(self.n*self.m)
        
    def sumOfRow(self,index):
        return sum(self.mat[index])
        
    def averageOfCol(self,index):
        Sum=0.0
        for i in range(self.n):
           Sum+=self.mat[i][index]
        return Sum/self.n
    
    def printGivenMatrix(self, matrix):
        for row in matrix:
            for element in row:
                print("  ",element, end=" ")
            print("")
            
    
    
    
    def subMatrix(self,col1,col2,row1,row2):
        subMat=[]
        for i in range(row1,row2):
           a=[]
           for j in range(col1,col2):
               a.append(self.mat[i][j])
           subMat.append(a)
        self.printGivenMatrix(subMat)
        
  
matrix=Matrix(4,4)
matrix.printMat()
print("Matrix mean: ",matrix.getMatMean())
print("Sum of row 1: ",matrix.sumOfRow(1))
print("Average of column 2 : ",matrix.averageOfCol(2))
print("Sub Matrix: ")
matrix.subMatrix(1,4,2,4)
