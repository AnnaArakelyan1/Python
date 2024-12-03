import random
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of '{func.__name__}': {end_time - start_time:.4f} seconds")
        return result
    return wrapper


@measure_time
def create_file_with_random_numbers(file_name="random_numbers.txt"):
    with open(file_name, "w") as f:
        for _ in range(100):
            line = " ".join(str(random.randint(1, 100)) for _ in range(20))
            f.write(line + "\n")
    print(f"File '{file_name}' created successfully.")


@measure_time
def process_and_write_back(file_name="random_numbers.txt"):
    with open(file_name, "r") as f:
        lines = f.readlines()
        integer_arrays = list(map(lambda line: list(map(int, line.split())), lines))
    
    filtered_lines = [
        " ".join(map(str, filter(lambda x: x > 40, array)))
        for array in integer_arrays
    ]
    
    with open(file_name, "w") as f:
        f.write("\n".join(filtered_lines) + "\n")
    print(f"Filtered data written back to '{file_name}'.")



def read_file_generator(file_name="random_numbers.txt"):
    with open(file_name, "r") as f:
        for line in f:
            yield list(map(int, line.split())) 

@measure_time
def process_with_generator(file_name="random_numbers.txt"):
    generator = read_file_generator(file_name)
    for line in generator:
        print(f"Processed Line: {line}") 



create_file_with_random_numbers()  
process_and_write_back()            
process_with_generator()          
