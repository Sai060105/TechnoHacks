import tkinter as tk
import random

def play_round():
    """Plays a single round of rock,  paper,  scissors."""
    user_choice = user_selection.get()

    # Get computer's choice randomly
    computer_choices = ["rock",  "paper",  "scissors"]
    computer_choice = random.choice(computer_choices)

    # Determine the winner
    if user_choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        result_label.config(text="You win!")
    else:
        result_label.config(text="Computer wins!")

    # Display choices
    user_choice_label.config(text=f"Your choice: {user_choice}")
    computer_choice_label.config(text=f"Computer choice: {computer_choice}")

# Create the main window
window = tk.Tk()
window.geometry("500x900")
window.config(bg="#33FFF1")
window.title("Rock Paper Scissors")

# Create labels
user_selection_label = tk.Label(window,  text="Choose your weapon:",font=("italic",  20,"bold"), bg='#ff000f')
user_selection_label.pack(pady=10)

user_selection = tk.StringVar(window)
user_selection.set("rock")  # Default choice

rock_button = tk.Radiobutton(
    window,  text="Rock",  font=("Arial",  15), bg='#ff00ff', variable=user_selection,  value="rock"
)
rock_button.pack(pady=10)

paper_button = tk.Radiobutton(
    window,  text="Paper",  font=("Arial",  15), bg='#ff00ff', variable=user_selection,  value="paper"
)
paper_button.pack(pady=10)

scissors_button = tk.Radiobutton(
    window,  text="Scissors",  font=("Arial",  15), bg='#ff00ff', variable=user_selection,  value="scissors"
)
scissors_button.pack(pady=10)

play_button = tk.Button(window,  text="Play",  fg='white',  bg='#38B6E8',  width=15, font=("Arial",  30), command=play_round)
play_button.pack(pady=10)

user_choice_label =  tk.Label(window, text="", anchor=tk.CENTER, bg="lightblue", height=3, width=30, bd=3, font=("Arial",  12,  "bold"), cursor="hand2", fg="red", padx=10, pady=10, justify=tk.CENTER, relief=tk.RAISED, wraplength=250)

user_choice_label.pack(pady=20)

computer_choice_label = tk.Label(window, text="", anchor=tk.CENTER, bg="lightblue", height=3, width=30, bd=3, font=("Arial",  12,  "bold"), cursor="hand2", fg="red", padx=10, pady=10, justify=tk.CENTER, relief=tk.RAISED, wraplength=250)
computer_choice_label.pack(pady=20)

result_label =  tk.Label(window, text="", anchor=tk.CENTER, bg="lightblue", height=3, width=30, bd=3, font=("Arial",  12,  "bold"), cursor="hand2", fg="red", padx=10, pady=10, justify=tk.CENTER, relief=tk.RAISED, wraplength=250)
result_label.pack(pady=20)

window.mainloop()
