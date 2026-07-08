import tkinter as tk
from tkinter import ttk, messagebox
import re
import random
import string


# ---------------- Password Strength Checker ---------------- #

def check_password():
    password = password_entry.get()

    if password == "":
        messagebox.showwarning("Warning", "Please enter a password.")
        return

    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("• Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("• Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("• Add at least one lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("• Add at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("• Add at least one special character.")

    progress["value"] = score * 20

    score_label.config(text=f"Security Score : {score}/5")

    if score <= 2:
        strength_label.config(text="🔴 WEAK", fg="red")
    elif score <= 4:
        strength_label.config(text="🟡 MEDIUM", fg="orange")
    else:
        strength_label.config(text="🟢 STRONG", fg="green")

    suggestion_box.delete("1.0", tk.END)

    if suggestions:
        suggestion_box.insert(tk.END, "Suggestions:\n\n")
        for item in suggestions:
            suggestion_box.insert(tk.END, item + "\n")
    else:
        suggestion_box.insert(
            tk.END,
            "Excellent!\nYour password is secure."
        )


# ---------------- Password Generator ---------------- #

def generate_password():
    length = int(length_spinbox.get())

    characters = (
        string.ascii_letters +
        string.digits +
        "!@#$%^&*()_+-=[]{}|;:,.<>?"
    )

    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*()_+-=[]{}|;:,.<>?")
    ]

    password += random.choices(characters, k=length - 4)

    random.shuffle(password)

    password = "".join(password)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


# ---------------- Copy Password ---------------- #

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied successfully!")


# ---------------- Clear ---------------- #

def clear_all():
    password_entry.delete(0, tk.END)
    suggestion_box.delete("1.0", tk.END)
    strength_label.config(text="")
    score_label.config(text="")
    progress["value"] = 0


# ---------------- Show / Hide ---------------- #

def toggle_password():
    if show_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")


# ---------------- GUI ---------------- #

root = tk.Tk()

root.title("Password Strength Analyzer")

root.geometry("700x650")

root.configure(bg="#f5f5f5")

title = tk.Label(
    root,
    text="Password Strength Analyzer",
    font=("Arial", 22, "bold"),
    bg="#f5f5f5"
)

title.pack(pady=15)

password_label = tk.Label(
    root,
    text="Enter Password",
    font=("Arial", 12),
    bg="#f5f5f5"
)

password_label.pack()

password_entry = tk.Entry(
    root,
    width=35,
    show="*",
    font=("Arial", 12)
)

password_entry.pack(pady=5)

show_var = tk.BooleanVar()

show_button = tk.Checkbutton(
    root,
    text="Show Password",
    variable=show_var,
    command=toggle_password,
    bg="#f5f5f5"
)

show_button.pack()

check_button = tk.Button(
    root,
    text="Check Password",
    width=20,
    bg="#007ACC",
    fg="white",
    command=check_password
)

check_button.pack(pady=10)

strength_label = tk.Label(
    root,
    text="",
    font=("Arial", 15, "bold"),
    bg="#f5f5f5"
)

strength_label.pack()

score_label = tk.Label(
    root,
    text="",
    font=("Arial", 12),
    bg="#f5f5f5"
)

score_label.pack()

progress = ttk.Progressbar(
    root,
    orient="horizontal",
    length=350,
    mode="determinate"
)

progress.pack(pady=10)

suggestion_box = tk.Text(
    root,
    width=65,
    height=8
)

suggestion_box.pack(pady=10)

generator_frame = tk.Frame(root, bg="#f5f5f5")
generator_frame.pack(pady=10)

tk.Label(
    generator_frame,
    text="Password Length",
    bg="#f5f5f5"
).grid(row=0, column=0)

length_spinbox = ttk.Spinbox(
    generator_frame,
    from_=8,
    to=32,
    width=5
)

length_spinbox.set(12)

length_spinbox.grid(row=0, column=1, padx=10)

generate_button = tk.Button(
    generator_frame,
    text="Generate Password",
    command=generate_password
)

generate_button.grid(row=0, column=2, padx=5)

copy_button = tk.Button(
    generator_frame,
    text="Copy Password",
    command=copy_password
)

copy_button.grid(row=0, column=3, padx=5)

clear_button = tk.Button(
    root,
    text="Clear",
    width=15,
    bg="red",
    fg="white",
    command=clear_all
)

clear_button.pack(pady=15)

root.mainloop()
