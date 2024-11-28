import os
def get_input():
    while True: 
        file_path = input("Enter the text file name you want to open: ").strip()
        try:
            if not file_path.endswith(".txt"):
                raise ValueError("File name must end with '.txt'.")
            
            base_name = file_path[:-4] 
            if not base_name.isnumeric():
                raise ValueError("File name must be numeric. Please try again.")

            with open(file_path, "r") as f:
                data = f.read()
                print("\nCurrent File Content:")
                print(data)

            choice = input("\nDo you want to write to the same file or a new file? (same/new): ").strip().lower()
            if choice == "same":
                write_to_file(file_path)  
            elif choice == "new":
                new_file_name = input("Enter the name of the new file: ").strip()
                new_content = input("Enter the content you want to write to the new file: ")
                write_to_file(new_file_name, new_content)
            else:
                print("Invalid choice. Please enter 'same' or 'new'.")
                continue

            return data

        except FileNotFoundError:
            print("The file you are trying to open does not exist. Please try again.")
        except ValueError as ve:
            print(f"ValueError: {ve}")


def write_to_file(file_name, content=None):
    try:  
        with open(file_name, "a") as f:
            if content is None:  
                content = input("Enter the content you want to write to the file: ")
            f.write(content + "\n") 
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print(f"Content successfully written to '{file_name}'.")
    finally:
        print(f"The file '{file_name}' has been closed.")


get_input()
