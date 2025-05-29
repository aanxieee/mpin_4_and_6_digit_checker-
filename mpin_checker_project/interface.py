import tkinter as tk
from tkinter import messagebox
from utils import check_common_and_demographic_mpin
from test_cases import run_test_cases_and_get_output

# ---------------------- windows setup -------------------------------------
root = tk.Tk()
root.title("Aanya's MPIN Strength Checker")
root.geometry("550x700")
root.configure(bg="#0b447e")

HEADER_FONT = ("Helvetica", 16, "bold")
LABEL_FONT = ("Helvetica", 12)
BUTTON_FONT = ("Helvetica", 11)
INPUT_BG = "#ed4bbd"

# --- variables ---
mpin_length_var = tk.IntVar(value=4)
is_married_var = tk.StringVar(value="No")
ask_demo = tk.BooleanVar()

# --- functions ---
def update_mpin_label():
    digits = mpin_length_var.get()
    mpin_label.config(text=f"Enter your {digits}-digit MPIN:")
    mpin_entry.delete(0, tk.END)

def toggle_marriage_fields():
    if is_married_var.get() == "Yes":
        spouse_dob_label.grid(row=5, column=0, sticky="e", padx=5, pady=5)
        spouse_dob_entry.grid(row=5, column=1, pady=5)
        anniversary_label.grid(row=6, column=0, sticky="e", padx=5, pady=5)
        anniversary_entry.grid(row=6, column=1, pady=5)
    else:
        spouse_dob_label.grid_remove()
        spouse_dob_entry.grid_remove()
        anniversary_label.grid_remove()
        anniversary_entry.grid_remove()

def evaluate_mpin():
    name = name_entry.get()
    mpin = mpin_entry.get()
    dob = dob_entry.get()
    spouse_dob = spouse_dob_entry.get() if is_married_var.get() == "Yes" else "0000-01-01"
    anniversary = anniversary_entry.get() if is_married_var.get() == "Yes" else "0000-01-01"

    required_len = mpin_length_var.get()
    if not mpin.isdigit() or len(mpin) != required_len:
        messagebox.showerror("Error", f"MPIN must be exactly {required_len} digits.")
        return

    if ask_demo.get():
        result = check_common_and_demographic_mpin(mpin, dob, spouse_dob, anniversary)
    else:
        result = check_common_and_demographic_mpin(mpin, "0000-01-01", "0000-01-01", "0000-01-01")

    feedback = f"\nHello {name or 'User'}, your MPIN is:\n\n"
    if result["strength"] == "STRONG":
        feedback += " STRONG — Looks good!\n"
    else:
        feedback += " WEAK\n\nReasons:\n"
        for reason in result["reasons"]:
            feedback += f"• {reason}\n"

    result_box.config(state="normal")
    result_box.delete(1.0, tk.END)
    result_box.insert(tk.END, feedback)
    result_box.config(state="disabled")

def run_tests_gui():
    outputs = run_test_cases_and_get_output()
    result_box.config(state="normal")
    result_box.delete(1.0, tk.END)
    for output in outputs:
        result_box.insert(tk.END, output + "\n" + ("-" * 50) + "\n")
    result_box.config(state="disabled")

# --- UI ;ayout ---
tk.Label(root, text=" Aanya's MPIN Strength Checker", font=HEADER_FONT, bg="#f0f4f8", fg="#333").pack(pady=10)

form_frame = tk.Frame(root, bg="#a13d8f")
form_frame.pack(pady=5)

# name
tk.Label(form_frame, text="Name:", font=LABEL_FONT, bg="#da3fbb").grid(row=0, column=0, sticky="e", padx=5, pady=5)
name_entry = tk.Entry(form_frame, width=30, bg=INPUT_BG)
name_entry.grid(row=0, column=1, pady=5)

# date of birth
tk.Label(form_frame, text="Your DOB (YYYY-MM-DD):", font=LABEL_FONT, bg="#f0f4f8").grid(row=1, column=0, sticky="e", padx=5, pady=5)
dob_entry = tk.Entry(form_frame, width=30, bg=INPUT_BG)
dob_entry.grid(row=1, column=1, pady=5)

# maritial status
tk.Label(form_frame, text="Are you married?", font=LABEL_FONT, bg="#f0f4f8").grid(row=2, column=0, sticky="e", padx=5, pady=5)
married_frame = tk.Frame(form_frame, bg="#da36c6")
married_frame.grid(row=2, column=1, pady=5)
tk.Radiobutton(married_frame, text="Yes", variable=is_married_var, value="Yes", bg="#f0f4f8", command=toggle_marriage_fields).pack(side="left", padx=5)
tk.Radiobutton(married_frame, text="No", variable=is_married_var, value="No", bg="#f0f4f8", command=toggle_marriage_fields).pack(side="left", padx=5)

# length of pin
tk.Label(form_frame, text="Select MPIN Length:", font=LABEL_FONT, bg="#f0f4f8").grid(row=3, column=0, sticky="e", padx=5, pady=5)
mpin_select_frame = tk.Frame(form_frame, bg="#df35bf")
mpin_select_frame.grid(row=3, column=1, pady=5)
tk.Radiobutton(mpin_select_frame, text="4-digit", variable=mpin_length_var, value=4, command=update_mpin_label, bg="#f0f4f8").pack(side="left", padx=5)
tk.Radiobutton(mpin_select_frame, text="6-digit", variable=mpin_length_var, value=6, command=update_mpin_label, bg="#f0f4f8").pack(side="left", padx=5)

# entry
mpin_label = tk.Label(form_frame, text="Enter your 4-digit MPIN:", font=LABEL_FONT, bg="#f0f4f8")
mpin_label.grid(row=4, column=0, sticky="e", padx=5, pady=5)
mpin_entry = tk.Entry(form_frame, width=30, bg=INPUT_BG)
mpin_entry.grid(row=4, column=1, pady=5)

# spouse dob
spouse_dob_label = tk.Label(form_frame, text="Spouse's DOB (YYYY-MM-DD):", font=LABEL_FONT, bg="#f0f4f8")
spouse_dob_entry = tk.Entry(form_frame, width=30, bg=INPUT_BG)

# anniversary
anniversary_label = tk.Label(form_frame, text="Anniversary (YYYY-MM-DD):", font=LABEL_FONT, bg="#f0f4f8")
anniversary_entry = tk.Entry(form_frame, width=30, bg=INPUT_BG)

# Demo checkbox
tk.Checkbutton(root, text="Check using demographic data?", variable=ask_demo, bg="#f0f4f8", font=("Helvetica", 10)).pack(pady=5)

# buttons
button_frame = tk.Frame(root, bg="#b42695")
button_frame.pack(pady=10)
tk.Button(button_frame, text="Check MPIN", command=evaluate_mpin, font=BUTTON_FONT, bg="#1e90ff", fg="white", padx=10).pack(side="left", padx=10)
tk.Button(button_frame, text="Run Test Cases", command=run_tests_gui, font=BUTTON_FONT, bg="#28a745", fg="white", padx=10).pack(side="left", padx=10)

# result box
result_box = tk.Text(root, height=10, width=65, state="disabled", bg="#e8f0fe", fg="#000", font=("Courier", 10))
result_box.pack(pady=10)

# init
toggle_marriage_fields()

# run 
root.mainloop()
