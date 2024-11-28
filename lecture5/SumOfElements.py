numbers_str=str(input("Enter numbers: ")).split()
numbers=[]
for x in numbers_str:
    numbers.append(int(x))
print(numbers)
answer=''
exclude_negative=True 
answer=str(input("Do you want to exclude the negative numbers?: "))
if(answer=="yes" or answer=="Yes"):
    exclude_negative=True 
else:
    exclude_negative=False
    
def sum_of_elements(numbers,exclude_negative):
        Sum=0
        for i in numbers:
          if(exclude_negative and i<0):
            continue
          Sum+=i

        return Sum

print(sum_of_elements(numbers,exclude_negative))
        
        
