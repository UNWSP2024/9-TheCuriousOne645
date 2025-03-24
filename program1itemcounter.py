def main():
    try:
        # Open the file in read mode
        with open("names.txt", "r") as file:
            # Read all lines from the file
            lines = file.readlines()
            
            # Count the number of lines (names) in the file
            num_names = len(lines)
        
        # Display the number of names
        print(f"The file contains {num_names} name(s).")
    except FileNotFoundError:
        print("Error: The file 'names.txt' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the program
if __name__ == "__main__":
    main()
