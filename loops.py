POUNDS_TO_KG = 0.45359237
INCHES_TO_METERS = 0.0254


def calculate_bmi(weight_pounds, height_inches):
    weight_kg = weight_pounds * POUNDS_TO_KG
    height_m = height_inches * INCHES_TO_METERS
    return weight_kg / (height_m ** 2)


def main():
    """Run the BMI calculator program with a loop."""
    while True:
        weight_pounds = float(input("Enter your weight in pounds: "))
        height_feet = int(input("Enter your height (feet): "))
        height_inches = int(input("Enter remaining inches: "))

        total_height_inches = (height_feet * 12) + height_inches
        bmi = calculate_bmi(weight_pounds, total_height_inches)

        print(f"Your BMI is {bmi:.2f}")

        choice = input("Do you want to calculate another BMI? (Y/N): ").strip().lower()
        if choice != "y":
            print("Goodbye!")
            break


main()
