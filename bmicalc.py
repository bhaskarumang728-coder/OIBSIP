import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight_kg = float(weight_entry.get())
        feet = int(feet_entry.get())
        inches = int(inches_entry.get())

        if weight_kg <= 0 or feet < 0 or inches < 0 or inches >= 12:
            messagebox.showerror("Invalid input", "Please enter valid positive numbers. Inches should be between 0 and 11.")
            return

        total_inches = feet * 12 + inches
        height_m = total_inches * 0.0254  # Convert inches to meters

        if height_m <= 0:
            messagebox.showerror("Invalid input", "Height must be greater than zero.")
            return

        bmi = weight_kg / (height_m ** 2)
        bmi = round(bmi, 1)
        category = classify_bmi(bmi)

        result_var.set(f"BMI: {bmi}  -  Category: {category}")

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numeric values.")

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

def reset_fields():
    weight_entry.delete(0, tk.END)
    feet_entry.delete(0, tk.END)
    inches_entry.delete(0, tk.END)
    result_var.set("")

# Setup main window
root = tk.Tk()
root.title("BMI Calculator (Feet & Inches)")
root.geometry("350x250")
root.resizable(False, False)

# Weight input
tk.Label(root, text="Weight (kg):").pack(pady=(15, 0))
weight_entry = tk.Entry(root)
weight_entry.pack()

# Height input - Feet
tk.Label(root, text="Height - Feet:").pack(pady=(10, 0))
feet_entry = tk.Entry(root)
feet_entry.pack()

# Height input - Inches
tk.Label(root, text="Height - Inches (0-11):").pack(pady=(10, 0))
inches_entry = tk.Entry(root)
inches_entry.pack()

# Result display
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 12), fg="blue")
result_label.pack(pady=10)

# Buttons frame
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

calc_btn = tk.Button(button_frame, text="Calculate BMI", command=calculate_bmi)
calc_btn.grid(row=0, column=0, padx=5)

reset_btn = tk.Button(button_frame, text="Reset", command=reset_fields)
reset_btn.grid(row=0, column=1, padx=5)

exit_btn = tk.Button(button_frame, text="Exit", command=root.destroy)
exit_btn.grid(row=0, column=2, padx=5)

root.mainloop()
