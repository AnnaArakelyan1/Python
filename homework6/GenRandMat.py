import random
rows=int(input("Enter the number of rows: "))
cols=int(input("Enter the number of columns: "))
mat=[]
def generate_random_matrix(rows,cols):
    for i in range(rows):
        a=[]
        for j in range(cols):
            a.append(random.randint(1,100))
        mat.append(a)

    return mat
            
print(generate_random_matrix(rows,cols))
    
