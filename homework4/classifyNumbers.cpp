numbers=[]
numbers_str = input("Enter the numbers of the list: ").split()
numbers = []
for x in numbers_str:
    numbers.append(int(x))

print(numbers)
even_numbers=[]
odd_numbers=[]
def classify_numbers(numbers):
    for i in numbers:
        if(i%2==0):
            even_numbers.append(i)
        else:
            odd_numbers.append(i)
            
    return even_numbers,odd_numbers
    
resOdd=[]
resEven=[]
resEven,resOdd=classify_numbers(numbers)
print("Even numbers: ",resEven,"  Odd numbers: ",resOdd)





