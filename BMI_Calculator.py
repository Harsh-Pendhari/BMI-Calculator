import tkinter as tk
from tkinter import font


def validate_numeric_input(P):
    if P == "":  # Allow empty string for backspace/delete
        return True

    # Ensure no leading/trailing spaces or other special characters
    if not all(char in "0123456789." for char in P):
        return False

    # Allow only one decimal
    if P.count('.') > 1:
        return False

    # avoid leading zeros unless it's just "0" or "0." followed by digits
    if len(P) > 1 and P.startswith('0') and P[1] != '.':
        return False

    try:
        # Convert to float to check for validity and is positive or not
        value = float(P)
        return value >= 0
    except ValueError:
        return False

def calculate():
    try:
        weight_str = weight_input.get()
        height_str = height_input.get()

        live_entry.config(fg="black")

        if (not weight_str) or (not height_str):
            entry_var.set("Please enter both weight and height.")
            live_entry.config(font = font.Font(size = 12), fg = "red")
            entry_var2.set("")
            return

        weight = float(weight_str)
        height_cm = float(height_str)

        if weight <= 0 or height_cm <= 0:
            entry_var.set("Weight and Height must be positive numbers.")
            live_entry.config(font = font.Font(size = 12), fg = "red")
            entry_var2.set("")
            return

        height_m = height_cm / 100
        
        bmi = weight / (height_m * height_m)
        result = f"{bmi:.2f}"

        live_entry.config(font = font.Font(size = 16))
        
        if bmi < 18.5:
            entry_var.set(f"Your BMI is {result}")
            entry_var2.set("You are Under Weight!")
            live_entry2.config(fg="red")

        elif 18.5 <= bmi < 24.9:
            entry_var.set(f"Your BMI is {result}")
            entry_var2.set("You have Healthy Weight!")
            live_entry2.config(fg="green")

        elif 24.9 <= bmi < 29.9:
            entry_var.set(f"Your BMI is {result}")
            entry_var2.set("You are Over Weight!")
            live_entry2.config(fg="orange")

        else: # bmi >= 29.9
            entry_var.set(f"Your BMI is {result}")
            entry_var2.set("You are obese!")
            live_entry2.config(fg="red")

    except ValueError:
        entry_var.set("Invalid input. Please enter valid numbers for weight and height.")
        live_entry.config(font = font.Font(size = 12), fg = "red")
        entry_var2.set("")

root = tk.Tk()
root.geometry("340x450")
root.title("BMI Calculator")
root.resizable(False, False)
root["bg"] = "lightgray"

entry_var = tk.StringVar(value="BMI will appear here")
entry_var2 = tk.StringVar(value="")
live_entry = tk.Label(root, textvariable=entry_var, font = font.Font(size=16), bg="lightgray")
live_entry.pack(padx=10, pady=(50,0), fill="x")

live_entry2 = tk.Label(root, textvariable=entry_var2, font = font.Font(size=16), bg="lightgray")
live_entry2.pack(padx=10, pady=(0,20), fill="x")

weight_label = tk.Label(root, text="Enter Weight (Kg) :", font=("Arial", 14), bg = "lightgray")
weight_label.pack()

vcmd = root.register(validate_numeric_input)
weight_input = tk.Entry(root, state="normal", font = font.Font(size=18), validate="key", validatecommand= (vcmd, '%P'))
weight_input.pack(padx= 15, fill="x")

height_label = tk.Label(root, text="Enter Height (cm) :", font=("Arial", 14), bg = "lightgray")
height_label.pack(pady=(20, 0))

vcmd = root.register(validate_numeric_input)
height_input = tk.Entry(root, state="normal", font = font.Font(size=18), validate="key", validatecommand= (vcmd, '%P'))
height_input.pack(padx= 15, fill="x")

calculate_btn = tk.Button(root, text="Calculate", font = font.Font(size=18), cursor="hand2", command=calculate)
calculate_btn.pack(pady=25)

root.mainloop()