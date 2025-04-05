def handle_file_error():
    filename = input("Please enter the filename: ")

    try:
        # Try to open and read the file
        with open(filename, "r") as file:
            content = file.read()
            print(f"File content:\n{content}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You don't have permission to read the file '{filename}'.")
    except IOError:
        print(f"Error: There was an issue opening or reading the file '{filename}'.")

# Example usage
handle_file_error()
