import secrets
import string
import tkinter as tk

# --------- COLORS ---------
bg_color = "#121212"
card_color = "#1C1C1C"
fg_color = "#E0E0E0"
button_bg = "#1E88E5"
button_hover = "#1565C0"
entry_bg = "#252525"

SAFE_SYMBOLS = "!@#$%^&*()-_=+[]{};:,.<>?"

# --------- WINDOW ---------
window = tk.Tk()
window.title("Password Generator")
window.geometry("420x650")
window.config(bg=bg_color)
window.resizable(False, False)

# --------- FUNCTIONS ---------
def generate_password():
    length = length_var.get()
    pools = []
    password = []

    if lowercase_var.get():
        pools.append(string.ascii_lowercase)
        password.append(secrets.choice(string.ascii_lowercase))
    if uppercase_var.get():
        pools.append(string.ascii_uppercase)
        password.append(secrets.choice(string.ascii_uppercase))
    if digits_var.get():
        pools.append(string.digits)
        password.append(secrets.choice(string.digits))
    if symbols_var.get():
        pools.append(SAFE_SYMBOLS)
        password.append(secrets.choice(SAFE_SYMBOLS))

    if not pools:
        show_notification("Select at least one option", "#E53935")
        update_strength_bar(0)
        return

    all_chars = "".join(pools)

    while len(password) < length:
        password.append(secrets.choice(all_chars))

    secrets.SystemRandom().shuffle(password)
    final_password = "".join(password)

    update_result(final_password)
    check_strength(final_password)
    copy_to_clipboard(final_password)
    show_notification("Password copied ✔", "#43A047")

def update_result(text):
    result_entry.config(state="normal")
    result_entry.delete(0, "end")
    result_entry.insert(0, text)
    result_entry.config(state="readonly")

def copy_to_clipboard(text):
    window.clipboard_clear()
    window.clipboard_append(text)

def show_notification(msg, color):
    notif_label.config(text=msg, bg=color)
    window.after(2000, lambda: notif_label.config(text="", bg=bg_color))

def check_strength(pwd):
    length = len(pwd)
    types = sum([
        any(c in string.ascii_lowercase for c in pwd),
        any(c in string.ascii_uppercase for c in pwd),
        any(c in string.digits for c in pwd),
        any(c in SAFE_SYMBOLS for c in pwd)
    ])

    score = length * 3 + types * 20
    if length < 8:
        score -= 20
    score = max(0, min(score, 100))

    label, color = (
        ("Weak", "#E53935") if score < 40 else
        ("Medium", "#FDD835") if score < 70 else
        ("Strong", "#43A047")
    )

    strength_label.config(text=f"Strength: {label}", fg=color)
    update_strength_bar(score)

def update_strength_bar(value):
    strength_canvas.delete("all")
    width = int(300 * value / 100)
    color = "#43A047" if value >= 70 else "#FDD835" if value >= 40 else "#E53935"
    strength_canvas.create_rectangle(0, 0, width, 10, fill=color, outline="")
    strength_canvas.create_rectangle(width, 0, 300, 10, fill="#333333", outline="")

def on_enter(e):
    e.widget.config(bg=button_hover)

def on_leave(e):
    e.widget.config(bg=button_bg)

# --------- TITLE ---------
tk.Label(window, text="🔐 Password Generator",
         font=("Segoe UI", 24, "bold"),
         bg=bg_color, fg=fg_color).pack(pady=20)

# --------- CARD ---------
card = tk.Frame(window, bg=card_color)
card.pack(padx=20, pady=10, fill="both", expand=True)

# --------- LENGTH ---------
tk.Label(card, text="Password Length",
         bg=card_color, fg=fg_color,
         font=("Segoe UI", 14, "bold")).pack(pady=(15, 5))

length_var = tk.IntVar(value=12)
length_value = tk.Label(card, text="12", bg=card_color, fg=fg_color)
length_value.pack()

def update_length(v):
    length_value.config(text=v)

tk.Scale(card, from_=5, to=50, orient="horizontal",
         variable=length_var,
         command=update_length,
         bg=card_color, fg=fg_color,
         troughcolor="#333333",
         highlightthickness=0).pack(padx=20)

# --------- OPTIONS ---------
options = tk.Frame(card, bg=card_color)
options.pack(pady=15)

lowercase_var = tk.BooleanVar(value=True)
uppercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar()

for text, var in [
    ("Lowercase letters", lowercase_var),
    ("Uppercase letters", uppercase_var),
    ("Numbers", digits_var),
    ("Symbols", symbols_var),
]:
    tk.Checkbutton(options, text=text, variable=var,
                   bg=card_color, fg=fg_color,
                   selectcolor=button_bg,
                   activebackground=card_color,
                   font=("Segoe UI", 11)).pack(anchor="w")

# --------- BUTTON ---------
btn = tk.Button(card, text="GENERATE PASSWORD",
                bg=button_bg, fg="white",
                font=("Segoe UI", 14, "bold"),
                bd=0, padx=10, pady=12,
                command=generate_password)
btn.pack(fill="x", padx=30, pady=20)
btn.bind("<Enter>", on_enter)
btn.bind("<Leave>", on_leave)

# --------- RESULT ---------
result_entry = tk.Entry(card, font=("Segoe UI", 16, "bold"),
                        bg=entry_bg, fg=fg_color,
                        justify="center", state="readonly")
result_entry.pack(fill="x", padx=30)

strength_label = tk.Label(card, text="", bg=card_color, fg=fg_color)
strength_label.pack(pady=8)

strength_canvas = tk.Canvas(card, width=300, height=10,
                            bg=card_color, highlightthickness=0)
strength_canvas.pack()

notif_label = tk.Label(card, text="", bg=bg_color, fg="white",
                       font=("Segoe UI", 10, "bold"))
notif_label.pack(pady=10)

window.mainloop()
