rows=int(input("Enter the number of rows: "))
cols=int(input("Enter the number of columns: "))
mat=[]

def generate_matrix(rows,cols):
    for i in range(rows):
        a=[]
        for j in range(cols):
            a.append(int(input()))
        mat.append(a)
    return mat
 
index=int(input("Enter the column index: "))   
def get_column_sum(mat,index):
    Sum=0
    for i in range(rows):
        Sum+=mat[i][index]
    return Sum
    
    
            
print(generate_matrix(rows,cols))
print("Sum: ",get_column_sum(mat,index))
  
