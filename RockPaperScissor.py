import tkinter as tk
import random

# Initialize scores
user_score = 0
comp_score = 0

# Game logic
def play(user_choice):
    global user_score, comp_score

    comp_choice = random.choice(["Rock", "Paper", "Scissors"])
    user_choice_label.config(text="You chose: " + user_choice)
    comp_choice_label.config(text="Computer chose: " + comp_choice)

    if user_choice == comp_choice:
        result_label.config(text="It's a Tie!", fg="orange")
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        result_label.config(text="You Win!", fg="green")
        user_score += 1
    else:
        result_label.config(text="You Lose!", fg="red")
        comp_score += 1

    score_label.config(text="Score - You: " + str(user_score) + " | Computer: " + str(comp_score))

# Reset function
def reset_game():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    user_choice_label.config(text="You chose:")
    comp_choice_label.config(text="Computer chose:")
    result_label.config(text="")
    score_label.config(text="Score - You: 0 | Computer: 0")

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")

# Title
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# Labels
user_choice_label = tk.Label(root, text="You chose:", font=("Arial", 12))
user_choice_label.pack(pady=5)

comp_choice_label = tk.Label(root, text="Computer chose:", font=("Arial", 12))
comp_choice_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack(pady=5)

# Reset Button
reset_btn = tk.Button(root, text="Reset Game", command=reset_game, bg="red", fg="white")
reset_btn.pack(pady=20)

# Start the GUI
root.mainloop()
