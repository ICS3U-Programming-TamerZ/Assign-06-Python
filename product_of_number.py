#!/usr/bin/env python3

# Created By: Tamer Zreg
# Date: Dec. 23rd, 2022
# This program gets user input as a list of floats
# Then it displays the product of the list rounded to two decimals.


import math


# Calculates the product of all elements in a list of floats
def product_of_list(list_of_floats):
    # Initialize product to 1
    product = 1

    # Return -1 if the length of the input list is 1
    if len(list_of_floats) == 1:
        return -1

    # Calculate product of all elements in list using a for loop
    else:
        for counter in range(0, len(list_of_floats)):
            product = list_of_floats[counter] * product

        # Round product to 2 decimal places
        product = round(product, 2)

        # Return -1 if product is equal to 1
        if product == 1:
            return -1

        # Return rounded product otherwise
        else:
            return product


def main():
    # Initialize empty list to store user input
    list_of_nums = []

    # Initialize variable to store user input
    number = None

    # Print program description
    print("This program multiplies the PRODUCT of numbers inside a list.")

    # Get user input until they enter -1
    while number != -1:
        try:
            # Get user input and convert to float
            number = float(input("Please enter a number (-1 to Stop): "))

            # Add input to list if it is not -1 and less than 10000
            if (number != -1) and (number < 10000):
                list_of_nums.append(number)
            # Error message if the number entered is greater than 10000
            elif number > 10000:
                print("Your number must be in range of 10000")
                main()
            # Calculate product of input list if user input is -1
            elif number == -1:
                product = product_of_list(list_of_nums)

                # Print error message if list has less than 2 elements
                if product == -1:
                    print("Please at least two numbers number")

                # Print product of input list otherwise
                else:
                    print(f"Your product amongst {list_of_nums} is {product}")

        # Handle exception if user input is not a number
        except ValueError:
            print("Please enter a number")
            main()


# Run main function if program is run directly
if __name__ == "__main__":
    main()
