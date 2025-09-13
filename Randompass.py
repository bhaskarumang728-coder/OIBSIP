import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be greater than zero.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid length.")
        return

    use_letters = letters_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()
    exclude_chars = exclude_entry.get()

    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Remove excluded characters
    for ch in exclude_chars:
        characters = characters.replace(ch, "")

    if not characters:
        messagebox.showerror("Error", "No valid characters available.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    pwd = password_entry.get()
    if not pwd:
        messagebox.showwarning("Warning", "No password to copy!")
        return
    root.clipboard_clear()
    root.clipboard_append(pwd)
    root.update()  # Keeps clipboard content after program closes
    messagebox.showinfo("Copied", "Password copied to clipboard.")

def reset_fields():
    length_entry.delete(0, tk.END)
    letters_var.set(True)
    digits_var.set(True)
    symbols_var.set(True)
    exclude_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("420x350")

# Length input
tk.Label(root, text="Password Length:").pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Checkboxes
letters_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters", variable=letters_var).pack()
tk.Checkbutton(root, text="Include Digits", variable=digits_var).pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack()

# Exclude characters
tk.Label(root, text="Exclude Characters:").pack()
exclude_entry = tk.Entry(root)
exclude_entry.pack()

# Buttons
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=5)
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)
tk.Button(root, text="Reset", command=reset_fields).pack(pady=5)

# Output password entry
password_entry = tk.Entry(root, width=40)
password_entry.pack()

root.mainloop()
