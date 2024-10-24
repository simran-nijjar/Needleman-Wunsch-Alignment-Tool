import tkinter as tk
from tkinter import messagebox
from needleman_wunsch_algorithm import needleman_wunsch
from idlelib.tooltip import Hovertip
from tkinter import ttk

# Method to check if string sequences are valid
def is_valid_sequence(seq):
    return all(char in 'ATGC' for char in seq)

# Method to check if match score is valid
def is_match_score_valid(match_score):
    return 0 <= match_score <= 10

# Method to check if penalties are valid
def is_penalty_valid(penalty):
    return -5 <= penalty <= -1

# Method to check fields and call needleman wunsch algorithm if all the fields are valid
def on_submit():
    seq1 = entry_seq1.get()
    seq2 = entry_seq2.get()

    # Convert sequence to uppercase
    seq1 = seq1.upper()
    seq2 = seq2.upper()

    if not seq1 or not seq2 or not is_valid_sequence(seq1) or not is_valid_sequence(seq2):
        messagebox.showerror("Input Error", "Enter a sequence that only use A,T,C, and G characters")
        return
    try:
        match_score = int(match_combobox.get())
        mismatch_score = int(mismatch_combobox.get())
        gap_penalty = int(gap_combobox.get())

        if not is_match_score_valid(match_score):
            messagebox.showerror("Input Error", "Match score must be between 0 and 10")
            return

        if not is_penalty_valid(mismatch_score):
            messagebox.showerror("Input Error", "Mistmatch/indel score must be between -5 and -1")
            return

        if not is_penalty_valid(gap_penalty):
            messagebox.showerror("Input Error", "Gap penalty must be between -5 and -1")
            return
    except ValueError:
        messagebox.showerror("Input Error", "Error with one or more of the inputs")
        return

    align1, align2, score, score_matrix = needleman_wunsch(seq1, seq2, match_score, mismatch_score, gap_penalty)
    result_label.config(text=f"Alignment 1: {align1}\nAlignment 2: {align2}\nScore: {score}")

    # Display the score matrix
    matrix_display = "\n".join(score_matrix)
    matrix_label.config(text=matrix_display)

# Create the main window
root = tk.Tk()
root.title("Needleman-Wunsch Alignment Tool")
root.resizable(False, False)

# Pop-up box labels

# Sequence 1
tk.Label(root, text="Sequence 1:").grid(row=0, column=0, padx=10, pady=10)
entry_seq1 = tk.Entry(root, width=30)
entry_seq1.grid(row=0, column=1, padx=10, pady=10)
seq1_tip = tk.Label(root, text="?", fg="blue")
seq1_tip.grid(row=0, column=2, padx=5, pady=10)
Hovertip(seq1_tip, 'Sequences must only contain A, T, C, or G')

# Sequence 2
tk.Label(root, text="Sequence 2:").grid(row=1, column=0, padx=10, pady=10)
entry_seq2 = tk.Entry(root, width=30)
entry_seq2.grid(row=1, column=1, padx=10, pady=10)
seq2_tip = tk.Label(root, text="?", fg="blue")
seq2_tip.grid(row=1, column=2, padx=5, pady=10)
Hovertip(seq2_tip, 'Sequences must only contain A, T, C, or G')

# Match score
tk.Label(root, text="Match Score:").grid(row=2, column=0, padx=10, pady=10)
match_values = [i for i in range(0, 11)]  # Values from 0 to 10
match_combobox = ttk.Combobox(root, values=match_values, state="readonly")
match_combobox.grid(row=2, column=1, padx=10, pady=10)
match_combobox.set(1)  # Default value
match_tip = Hovertip(match_combobox, 'Match score must be between 0 and 10')

# Mismatch/Indel score
tk.Label(root, text="Mismatch/Indel Score:").grid(row=3, column=0, padx=10, pady=10)
mismatch_values = [i for i in range(-5, 0)]  # Values from -5 to -1
mismatch_combobox = ttk.Combobox(root, values=mismatch_values, state="readonly")
mismatch_combobox.grid(row=3, column=1, padx=10, pady=10)
mismatch_combobox.set(-1)  # Default value
mismatch_tip = Hovertip(mismatch_combobox, 'Mismatch/indel score must be between -5 and -1')

# Gap penalty
tk.Label(root, text="Gap Penalty:").grid(row=4, column=0, padx=10, pady=10)
gap_values = [i for i in range(-5, 0)]  # Values from -5 to -1
gap_combobox = ttk.Combobox(root, values=gap_values, state="readonly")
gap_combobox.grid(row=4, column=1, padx=10, pady=10)
gap_combobox.set(-1)  # Default value
gap_tip = Hovertip(gap_combobox, 'Gap penalty must be between -5 and -1')

# Align button
align_button = tk.Button(root, text="Align", command=on_submit)
align_button.grid(row=5, column=1, padx=10, pady=20)

# Alignment output
result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Score matrix output
tk.Label(root, text="Score Matrix:").grid(row=7, column=0, padx=10, pady=10)
matrix_label = tk.Label(root, text="", justify=tk.LEFT, anchor="nw", font=("Courier", 10))
matrix_label.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

# Run the GUI event loop
root.mainloop()
