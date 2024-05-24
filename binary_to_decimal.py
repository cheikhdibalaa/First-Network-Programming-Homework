# Convert a binary string to a decimal number
def binary_to_decimal(binary_str):
    try:
        # The int function converts binary to decimal
        decimal_number = int(binary_str, 2)
        # Return the decimal number if conversion is successful
        return decimal_number
    except ValueError:
        # If there is a ValueError (invalid binary string), return None
        return None


# Repeatedly ask the user for a binary number and convert it to decimal
def start_change():
    while True:  # Start an infinite loop to keep asking the user for input
        # Prompt the user to enter a binary number
        binary_str = input("Enter a binary number: ")
        # Call the binary_to_decimal function to convert the binary string to a decimal number
        decimal_number = binary_to_decimal(binary_str)
        if decimal_number is not None:  # Check if the conversion was successful
            # Print the decimal equivalent of the binary number
            print(f"The decimal equivalent of binary {binary_str} is {decimal_number}")
            # Break the loop as a valid binary number was entered and processed
            break
        else:
            # Inform the user that the input was invalid and prompt again
            print("Invalid binary number. Please enter a valid binary number.")
