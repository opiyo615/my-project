def modify_(line):
    # EXAMPLE modification: convert to uppercase
    return line.upper()

def main():
    # Ask the user for the input file name
    input_file = input("Enter the name of the input file to read from: ")

    try:
        # Try to open the file for reading
        with open(input_file, 'r') as infile:
            # Read all lines and modify them
            modified_lines = 
            [modify_ line(line) for line in infile]

        #Create a new output file name
        Output _file = "modified_" + input_file

        # Write the modified content to a new file
        with open(Output_file, 'w') as outfile:
            outfile.writelines(modified_lines)
            print(f"Modified content written to {Output_file} ' successfully.")

    except FileNotFoundError:
        print(X"Error: The file '{input_file}' was not found.")

    except 10Error:
        print("X Error : An 1/10 error occured while reading or writing the file.")
        except Exception as e:
        print(f" X unexpected error: {e}")

if __name__ == "__main__":
    main()
    



