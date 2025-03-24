def main():
    try:
        # Open the file in read mode
        with open("numbers.txt", "r") as file:
            total = 0
            count = 0
            
            # Iterate through each line in the file
            for line in file:
                try:
                    # Convert line to an integer and add to total
                    number = int(line.strip())
                    total += number
                    count += 1
                except ValueError:
                    print(f"Warning: Invalid value encountered ('{line.strip()}'). Skipping...")
        
        # Display the total and average
        print(f"Total of numbers: {total}")
        if count > 0:
            print(f"Average of numbers: {total / count:.2f}")
        else:
            print("No valid numbers to calculate the average.")
    
    except IOError:
        print("Error: Unable to access or read the file 'numbers.txt'. Please check its existence and permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    main()
