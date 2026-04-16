# This program creates a simple GUI data entry form.
# The user enters their name and the number of hours worked.
# When the button is clicked, the program checks whether the hours entered
# are numeric. If not, it shows an error message and stops.
# If valid, it calculates weekly pay and displays the result.

import tkinter as tk
from tkinter import messagebox

# Function to process the form when the button is clicked
def calculate_pay():
    # Get the user's name from the text box
    name = name_entry.get()

    # Get the hours worked from the text box
    hours_text = hours_entry.get()

    # Validate that the hours entered is numeric
    try:
        hours = float(hours_text)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for hours worked.")
        return  # Stop the program from going further

    # Perform a calculation
    hourly_rate = 15
    pay = hours * hourly_rate

    # String manipulation: make name title case
    formatted_name = name.title()

    # Show the result in the output label
    result_label.config(
        text=f"Employee: {formatted_name}\nHours Worked: {hours}\nWeekly Pay: ${pay:.2f}"
    )

# Create the main window
window = tk.Tk()
window.title("Employee Pay Calculator")
window.geometry("350x250")

# Form instructions
instruction_label = tk.Label(window, text="Enter employee information below:")
instruction_label.pack(pady=10)

# Name label and entry box
name_label = tk.Label(window, text="Employee Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

# Hours worked label and entry box
hours_label = tk.Label(window, text="Hours Worked:")
hours_label.pack()
hours_entry = tk.Entry(window)
hours_entry.pack()

# Button to calculate pay
calc_button = tk.Button(window, text="Calculate Pay", command=calculate_pay)
calc_button.pack(pady=10)

# Label to display output/results
result_label = tk.Label(window, text="", justify="left")
result_label.pack(pady=10)

# Run the GUI application
window.mainloop()
