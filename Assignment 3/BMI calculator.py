"""
Assignment 3 - BMI Calculator

This program calculates Body Mass Index (BMI) using user input.
It follows Python coding standards:
- Variable and function names use snake_case (PEP 8)
- Functions are documented using docstrings (PEP 257)
"""

POUNDS_TO_KG = 0.45359237
INCHES_TO_METERS = 0.0254


def calculate_bmi(weight_pounds, height_inches):
    """
    Calculate BMI using weight in pounds and height in inches.

    Args:
        weight_pounds (float): Weight in pounds
        height_inches (float): Height in inches

    Returns:
        float: Calculated BMI value
    """
    weight_kg = weight_pounds * POUNDS_TO_KG
    height_m = height_inches * INCHES_TO_METERS
    bmi = weight_kg / (height_m ** 2)
    return bmi


def main():
    """Run the BMI calculator program."""
    weight_pounds = float(input("Enter your weight in pounds: "))
    height_feet = int(input("Enter your height (feet): "))
    height_inches = int(input("Enter remaining inches: "))

    total_height_inches = (height_feet * 12) + height_inches
    bmi = calculate_bmi(weight_pounds, total_height_inches)

    print(f"Your BMI is {bmi:.2f}")


main()
