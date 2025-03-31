#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: Mar. 31, 2025
"""
This program asks the user for a subtotal.
It then calculates and displays the tax and total
based on the Nova Scotia HST (15%).
"""

# Import the constants module to utilize the tax rate.
import constants


# Define the main function.
def main():
    # Get the subtotal from the user.
    subtotal = float(input("Enter the desired subtotal: $"))

    # Calculate the tax, multiplying it with the Nova Scotia HST rate (15%).
    tax = subtotal * constants.HST_RATE

    # Calculate the total.
    total = subtotal + tax

    # Display the tax to the user.
    print(f"The tax is ${tax:.2f}.")
    # Display the total to the user.
    print(f"The total cost is ${total:.2f}.")


# Check if the special name of the file is __main__.
if __name__ == "__main__":
    # Run the main function if so.
    main()
