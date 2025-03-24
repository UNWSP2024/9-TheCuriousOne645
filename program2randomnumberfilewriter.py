import random

def main():
    # Prompt the user for the number of random numbers
    try:
        num_numbers = int(input("Enter how many random numbers the file will hold (1-1000): "))
        if num_numbers < 1 or num_numbers > 1000:
            print("Please enter a number between 1 and 1000.")
            return
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return

    # Open a file to write
    with open("random_numbers.txt", "w") as file:
        # Generate random numbers and write them to the file
        for _ in range(num_numbers):
            file.write(f"{random.randint(1, 500)}\n")
    
    print(f"Successfully written {num_numbers} random numbers to 'random_numbers.txt'.")

# Run the program
if __name__ == "__main__":
    main()
