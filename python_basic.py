def basic_A():
    # Create and print a dictionary from two lists
    # List of protocol names
    L1 = ["HTTP", "HTTPS", "FTP", "DNS"]
    # List of port numbers
    L2 = [80, 443, 21, 53]

    # The zip function combines L1 and L2 into pairs like (HTTP, 80), (HTTPS, 443), etc.
    # The dict function then creates a dictionary from these pairs
    d = dict(zip(L1, L2))

    # Print the created dictionary
    print(d)


def basic_B():
    # Calculate the factorial of a number

    # Nested function to calculate factorial of a given number using recursion
    # A factorial of a number n is the product of all positive integers less than or equal to n
    def factorial(n):
        if n == 0:  # Base case: the factorial of 0 is defined to be 1
            return 1
        else:  # Recursive case: the factorial of n is n times the factorial of (n - 1)
            return n * factorial(n - 1)

    # input() function reads a string from the user, and int() converts it to an integer
    number = int(input("Enter a number to calculate its factorial: "))

    # Call the factorial function with the user's number and store the result
    result = factorial(number)

    # Print the result of the factorial calculation
    print(f"The factorial of {number} is {result}")



def basic_C():
    # print items from a list that start with the letter 'B'
    # List of words to check
    L = ["Network", "Bio", "Programming", "Physics", "Music"]

    # Loop through each item in the list
    for item in L:
        # Check if the item starts with the letter 'B'
        # startswith() is a string method that returns True if the string starts with the specified prefix
        if item.startswith("B"):
            # Print the item if it starts with 'B'
            print(item)

def basic_D():
    # create a dictionary using dictionary comprehension
    # the keys are numbers from 0 to 10, and the values are the keys plus 1
    # The range(11) function generates numbers from 0 to 10 (inclusive)
    d = {i: i + 1 for i in range(11)}

    # Print the created dictionary
    print(d)
