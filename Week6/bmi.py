def calculate_bmi(weight, height):
    if height <= 0:
        raise ValueError("Height must be greater than zero.")
    if weight <= 0:
        raise ValueError("Weight must be greater than zero.")

    bmi = (weight / (height ** 2)) * 703
    return round(bmi, 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


# Optional interactive run
if __name__ == "__main__":
    weight = float(input("Enter weight (lbs): "))
    height = float(input("Enter height (inches): "))

    bmi = calculate_bmi(weight, height)
    print("BMI:", bmi)
    print("Category:", bmi_category(bmi))
