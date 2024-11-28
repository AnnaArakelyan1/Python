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
 
index=int(input("Enter the row index: "))   
def get_row_average(mat,index):
    Sum = sum(mat[index])
    return Sum / len(mat[index]) 
    
    
            
print(generate_matrix(rows,cols))
print("Average of row ",index,": ",get_row_average(mat,index))
  
