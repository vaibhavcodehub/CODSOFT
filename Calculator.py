import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("320x480")
root.config(bg="#1e1e1e")
root.resizable(False, False)

# Entry widget for display
entry = tk.Entry(
    root,
    font=("Helvetica", 24),
    bd=0,
    bg="#2e2e2e",
    fg="white",
    justify="right",
    relief="flat"
)
entry.pack(pady=15, padx=10, fill="x", ipady=12)

# Frame for buttons
btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(padx=5, pady=5)

# Button layout (organized for correct grid placement)
buttons = [
    ["AC", "⌫", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "="]
]

# Command to handle button press
def on_click(value):
    current = entry.get()
    if value == "=":
        try:
            result = eval(current.replace("×", "*").replace("÷", "/"))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif value == "AC":
        entry.delete(0, tk.END)
    elif value == "⌫":
        entry.delete(len(current)-1, tk.END)
    else:
        entry.insert(tk.END, value)

# Button colors
btn_colors = {
    "AC": "#ff6666", "⌫": "#ff9966", "%": "#66b3ff", "÷": "#66b3ff",
    "×": "#66b3ff", "-": "#66b3ff", "+": "#66b3ff", "=": "#4cd137"
}

# Create and place buttons
for i, row in enumerate(buttons):
    for j, char in enumerate(row):
        if i == 4:  # Last row with "0", ".", "="
            if char == "0":
                btn = tk.Button(
                    btn_frame, text=char, font=("Helvetica", 16), width=12, height=2,
                    fg="white", bg="#333333", bd=0, activebackground="#555555",
                    command=lambda val=char: on_click(val)
                )
                btn.grid(row=i, column=0, columnspan=2, padx=4, pady=4, sticky="nsew")
            elif char == ".":
                btn = tk.Button(
                    btn_frame, text=char, font=("Helvetica", 16), width=5, height=2,
                    fg="white", bg="#333333", bd=0, activebackground="#555555",
                    command=lambda val=char: on_click(val)
                )
                btn.grid(row=i, column=2, padx=4, pady=4, sticky="nsew")
            elif char == "=":
                btn = tk.Button(
                    btn_frame, text=char, font=("Helvetica", 16), width=5, height=2,
                    fg="white", bg=btn_colors.get("=", "#4cd137"), bd=0,
                    activebackground="#555555",
                    command=lambda val=char: on_click(val)
                )
                btn.grid(row=i, column=3, padx=4, pady=4, sticky="nsew")
        else:
            btn = tk.Button(
                btn_frame, text=char, font=("Helvetica", 16), width=5, height=2,
                fg="white", bg=btn_colors.get(char, "#333333"), bd=0,
                activebackground="#555555",
                command=lambda val=char: on_click(val)
            )
            btn.grid(row=i, column=j, padx=4, pady=4, sticky="nsew")

# Run the app
root.mainloop()
