def read_and_write_file(input_filename, output_filename):
    try:
        # Open the input file to read
        with open(input_filename, "r") as infile:
            content = infile.read()  # Read the entire content of the file

        # Modify the content (example: converting all text to uppercase)
        modified_content = content.upper()

        # Write the modified content to the output file
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"Content has been modified and written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    except IOError:
        print(f"Error: There was an issue reading or writing the files.")

# Example usage
input_file = "input.txt"  # Change to your file
output_file = "output.txt"  # The new file to write to
read_and_write_file(input_file, output_file)
