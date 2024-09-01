# algorithm_gui.py

import tkinter as tk
from tkinter import messagebox
from needleman_wunsch_algorithm import needleman_wunsch

def on_submit():
    seq1 = entry_seq1.get()
    seq2 = entry_seq2.get()
    try:
        match_score = int(entry_match.get())
        mismatch_score = int(entry_mismatch.get())
        gap_penalty = int(entry_gap.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid characters")
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

tk.Label(root, text="Sequence 2:").grid(row=1, column=0, padx=10, pady=10)
entry_seq2 = tk.Entry(root, width=30)
entry_seq2.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Match Score:").grid(row=2, column=0, padx=10, pady=10)
entry_match = tk.Entry(root, width=10)
entry_match.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Mismatch/Indel Score:").grid(row=3, column=0, padx=10, pady=10)
entry_mismatch = tk.Entry(root, width=10)
entry_mismatch.grid(row=3, column=1, padx=10, pady=10)

tk.Label(root, text="Gap Penalty:").grid(row=4, column=0, padx=10, pady=10)
entry_gap = tk.Entry(root, width=10)
entry_gap.grid(row=4, column=1, padx=10, pady=10)

submit_button = tk.Button(root, text="Align", command=on_submit)
submit_button.grid(row=5, column=1, padx=10, pady=20)

result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Run the GUI event loop
root.mainloop()