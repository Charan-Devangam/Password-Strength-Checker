import tkinter as tk
from tkinter import ttk
import random
import string


# ==========================================
# PASSWORD CHECK FUNCTION
# ==========================================

def check_password():
    password = password_entry.get()

    # Empty password check
    if password == "":
        result_label.config(
            text="Please enter a password",
            fg="red"
        )

        requirements_label.config(text="")
        strength_bar["value"] = 0
        return

    # Character checks
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

    # Check every character
    for char in password:

        if char.isupper():
            has_upper = True

        if char.islower():
            has_lower = True

        if char.isdigit():
            has_digit = True

        if char in special_characters:
            has_special = True

    # ==========================================
    # SCORE
    # ==========================================

    score = 0

    # Length
    if len(password) >= 8:
        score += 1

    # 12 characters bonus
    if len(password) >= 12:
        score += 1

    # Uppercase
    if has_upper:
        score += 1

    # Lowercase
    if has_lower:
        score += 1

    # Number
    if has_digit:
        score += 1

    # Special character
    if has_special:
        score += 1

    # ==========================================
    # STRENGTH
    # ==========================================

    if score <= 2:
        strength = "WEAK"
        strength_color = "red"

    elif score <= 4:
        strength = "MEDIUM"
        strength_color = "orange"

    else:
        strength = "STRONG"
        strength_color = "green"

    # Update progress bar
    strength_bar["value"] = score

    # Display result
    result_label.config(
        text=f"Strength: {strength}\nScore: {score}/6",
        fg=strength_color
    )

    # ==========================================
    # REQUIREMENTS
    # ==========================================

    requirements = ""

    if len(password) >= 8:
        requirements += "✓ At least 8 characters\n"
    else:
        requirements += "✗ At least 8 characters\n"

    if len(password) >= 12:
        requirements += "✓ 12 or more characters\n"
    else:
        requirements += "✗ 12 or more characters\n"

    if has_upper:
        requirements += "✓ Uppercase letter\n"
    else:
        requirements += "✗ Uppercase letter\n"

    if has_lower:
        requirements += "✓ Lowercase letter\n"
    else:
        requirements += "✗ Lowercase letter\n"

    if has_digit:
        requirements += "✓ Number\n"
    else:
        requirements += "✗ Number\n"

    if has_special:
        requirements += "✓ Special character\n"
    else:
        requirements += "✗ Special character\n"

    # ==========================================
    # COMMON PASSWORD CHECK
    # ==========================================

    common_passwords = [
        "password",
        "12345678",
        "123456789",
        "qwerty",
        "password123",
        "admin",
        "welcome",
        "letmein"
    ]

    if password.lower() in common_passwords:
        requirements += "\n⚠ WARNING: Common password!"

    requirements_label.config(
        text=requirements
    )


# ==========================================
# SHOW / HIDE PASSWORD
# ==========================================

def toggle_password():

    if password_entry.cget("show") == "*":

        password_entry.config(show="")
        show_button.config(text="HIDE")

    else:

        password_entry.config(show="*")
        show_button.config(text="SHOW")


# ==========================================
# GENERATE STRONG PASSWORD
# ==========================================

def generate_password():

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    special = "!@#$%^&*"

    # Guarantee at least one from each category
    password_characters = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(numbers),
        random.choice(special)
    ]

    # Remaining 8 characters
    all_characters = uppercase + lowercase + numbers + special

    for i in range(8):
        password_characters.append(
            random.choice(all_characters)
        )

    # Shuffle characters
    random.shuffle(password_characters)

    # Convert list to string
    password = "".join(password_characters)

    # Put generated password into entry box
    password_entry.delete(0, tk.END)

    password_entry.insert(
        0,
        password
    )

    # Automatically check generated password
    check_password()


# ==========================================
# CLEAR / RESET
# ==========================================

def clear_all():

    password_entry.delete(
        0,
        tk.END
    )

    result_label.config(
        text="",
        fg="black"
    )

    requirements_label.config(
        text=""
    )

    strength_bar["value"] = 0


# ==========================================
# MAIN WINDOW
# ==========================================

window = tk.Tk()

window.title(
    "Password Strength Checker"
)

window.geometry(
    "550x700"
)

window.configure(
    bg="#f2f2f2"
)

# ==========================================
# TITLE
# ==========================================

title = tk.Label(
    window,
    text="PASSWORD STRENGTH CHECKER",
    font=("Arial", 22, "bold"),
    bg="#f2f2f2"
)

title.pack(
    pady=35
)


# ==========================================
# PASSWORD LABEL
# ==========================================

password_label = tk.Label(
    window,
    text="Enter Password:",
    font=("Arial", 12),
    bg="#f2f2f2"
)

password_label.pack()


# ==========================================
# PASSWORD FRAME
# ==========================================

password_frame = tk.Frame(
    window,
    bg="#f2f2f2"
)

password_frame.pack(
    pady=10
)


# ==========================================
# PASSWORD ENTRY
# ==========================================

password_entry = tk.Entry(
    password_frame,
    width=25,
    font=("Arial", 14),
    show="*"
)

password_entry.pack(
    side="left"
)


# ==========================================
# SHOW BUTTON
# ==========================================

show_button = tk.Button(
    password_frame,
    text="SHOW",
    font=("Arial", 10),
    command=toggle_password
)

show_button.pack(
    side="left",
    padx=5
)


# ==========================================
# CHECK BUTTON
# ==========================================

check_button = tk.Button(
    window,
    text="CHECK PASSWORD",
    font=("Arial", 12, "bold"),
    command=check_password
)

check_button.pack(
    pady=15
)


# ==========================================
# GENERATE BUTTON
# ==========================================

generate_button = tk.Button(
    window,
    text="GENERATE PASSWORD",
    font=("Arial", 12),
    command=generate_password
)

generate_button.pack(
    pady=5
)


# ==========================================
# CLEAR BUTTON
# ==========================================

clear_button = tk.Button(
    window,
    text="CLEAR",
    font=("Arial", 12),
    command=clear_all
)

clear_button.pack(
    pady=5
)


# ==========================================
# STRENGTH RESULT
# ==========================================

result_label = tk.Label(
    window,
    text="",
    font=("Arial", 16, "bold"),
    bg="#f2f2f2"
)

result_label.pack(
    pady=15
)


# ==========================================
# STRENGTH BAR
# ==========================================

strength_bar = ttk.Progressbar(
    window,
    length=300,
    maximum=6,
    mode="determinate"
)

strength_bar.pack(
    pady=5
)


# ==========================================
# REQUIREMENTS TITLE
# ==========================================

requirements_title = tk.Label(
    window,
    text="Requirements:",
    font=("Arial", 14, "bold"),
    bg="#f2f2f2"
)

requirements_title.pack(
    pady=15
)


# ==========================================
# REQUIREMENTS RESULT
# ==========================================

requirements_label = tk.Label(
    window,
    text="",
    font=("Arial", 12),
    justify="left",
    bg="#f2f2f2"
)

requirements_label.pack()


# ==========================================
# START GUI
# ==========================================

window.mainloop()