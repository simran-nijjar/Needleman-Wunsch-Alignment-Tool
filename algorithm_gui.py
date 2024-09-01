# algorithm_gui.py

import tkinter as tk
from tkinter import messagebox
from needleman_wunsch_algorithm import needleman_wunsch
from idlelib.tooltip import Hovertip

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

    if not is_valid_sequence(seq1) or not is_valid_sequence(seq2):
        messagebox.showerror("Input Error", "Sequences must only contain A, T, C, or G")
        return
    try:
        match_score = int(entry_match.get())
        mismatch_score = int(entry_mismatch.get())
        gap_penalty = int(entry_gap.get())

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

    align1, align2, score = needleman_wunsch(seq1, seq2, match_score, mismatch_score, gap_penalty)
    result_label.config(text=f"Alignment 1: {align1}\nAlignment 2: {align2}\nScore: {score}")

# Create the main window
root = tk.Tk()
root.title("Needleman-Wunsch Alignment Tool")

# Pop-up box labels
tk.Label(root, text="Sequence 1:").grid(row=0, column=0, padx=10, pady=10)
entry_seq1 = tk.Entry(root, width=30)
entry_seq1.grid(row=0, column=1, padx=10, pady=10)
seq1_tip = tk.Label(root, text="?", fg="blue")
seq1_tip.grid(row=0, column=2, padx=5, pady=10)
Hovertip(seq1_tip, 'Sequences must only contain A, T, C, or G')

tk.Label(root, text="Sequence 2:").grid(row=1, column=0, padx=10, pady=10)
entry_seq2 = tk.Entry(root, width=30)
entry_seq2.grid(row=1, column=1, padx=10, pady=10)
seq2_tip = tk.Label(root, text="?", fg="blue")
seq2_tip.grid(row=1, column=2, padx=5, pady=10)
Hovertip(seq2_tip, 'Sequences must only contain A, T, C, or G')

tk.Label(root, text="Match Score:").grid(row=2, column=0, padx=10, pady=10)
entry_match = tk.Entry(root, width=10)
entry_match.grid(row=2, column=1, padx=10, pady=10)
match_tip = tk.Label(root, text="?", fg="blue")
match_tip.grid(row=2, column=2, padx=5, pady=10)
Hovertip(match_tip, 'Match score must be between 0 and 10')

tk.Label(root, text="Mismatch/Indel Score:").grid(row=3, column=0, padx=10, pady=10)
entry_mismatch = tk.Entry(root, width=10)
entry_mismatch.grid(row=3, column=1, padx=10, pady=10)
mismatch_tip = tk.Label(root, text="?", fg="blue")
mismatch_tip.grid(row=3, column=2, padx=5, pady=10)
Hovertip(mismatch_tip, 'Mismatch/indel score must be between -5 and -1')

tk.Label(root, text="Gap Penalty:").grid(row=4, column=0, padx=10, pady=10)
entry_gap = tk.Entry(root, width=10)
entry_gap.grid(row=4, column=1, padx=10, pady=10)
gap_tip = tk.Label(root, text="?", fg="blue")
gap_tip.grid(row=4, column=2, padx=5, pady=10)
Hovertip(gap_tip, 'Gap penalty must be between -5 and -1')

submit_button = tk.Button(root, text="Align", command=on_submit)
submit_button.grid(row=5, column=1, padx=10, pady=20)

result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Run the GUI event loop
root.mainloop()