#!/usr/bin/env python3

# Created By: Tamer Zreg
# Date: Dec. 23rd, 2022
# This  program gets user input as a list of floats
# Then it adds the product of the list rounded to two decimals to a test file.


def calculate_product(numbers: list) -> float:
    # Calculate the product of the numbers
    product = 1
    for number in numbers:
        product *= number

    return product


def main():
    from random import randint

    numbers = []
    # Create a list of random numbers and opens a file of them.
    for counter in range(0, 10):
        number = randint(1, 10)
        numbers.append(number)
        with open("numbers.txt", "w") as output_file:
            output_file.write(f"The numbers are {str(numbers)}")

    # Calculate the product of the numbers
    product = calculate_product(numbers)

    # Open the output file and write the product
    with open("product.txt", "w") as output_file:
        output_file.write(f"The product is {str(product)}")


if __name__ == "__main__":
    main()
