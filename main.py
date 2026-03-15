import tkinter as tk
import random

# possible choices
options = ["Rock", "Paper", "Scissors"]

# scores
player_score = 0
computer_score = 0


# function that runs when a button is clicked
def game(choice):
    global player_score, computer_score

    # computer randomly chooses
    comp = random.choice(options)

    # show choices on screen
    player_choice_label.config(text="You chose: " + choice)
    computer_choice_label.config(text="Computer chose: " + comp)

    # decide winner
    if choice == comp:
        result = "Tie!"

    elif (choice == "Rock" and comp == "Scissors") or \
         (choice == "Paper" and comp == "Rock") or \
         (choice == "Scissors" and comp == "Paper"):

        result = "You Win!"
        player_score += 1

    else:
        result = "Computer Wins!"
        computer_score += 1

    # update result and score
    result_label.config(text=result)
    score_label.config(text="Score -  You:{}  Computer:{}".format(player_score, computer_score))


# create main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("480x380")
root.configure(bg="black")


# title
title = tk.Label(root,
                 text="Rock Paper Scissors",
                 font=("Arial", 22, "bold"),
                 bg="black",
                 fg="white")
title.pack(pady=20)


# label to show player choice
player_choice_label = tk.Label(root,
                               text="",
                               font=("Arial", 13),
                               bg="black",
                               fg="white")
player_choice_label.pack()


# label to show computer choice
computer_choice_label = tk.Label(root,
                                 text="",
                                 font=("Arial", 13),
                                 bg="black",
                                 fg="white")
computer_choice_label.pack()


# result label
result_label = tk.Label(root,
                        text="Choose your move",
                        font=("Arial", 15, "bold"),
                        bg="black",
                        fg="cyan")
result_label.pack(pady=12)


# score label
score_label = tk.Label(root,
                       text="Score  You:0  Computer:0",
                       font=("Arial", 13),
                       bg="black",
                       fg="white")
score_label.pack(pady=8)


# frame for buttons
frame = tk.Frame(root, bg="black")
frame.pack(pady=25)


# buttons
rock_btn = tk.Button(frame,
                     text="Rock",
                     width=10,
                     font=("Arial", 11, "bold"),
                     bg="red",
                     fg="white",
                     command=lambda: game("Rock"))
rock_btn.grid(row=0, column=0, padx=8)


paper_btn = tk.Button(frame,
                      text="Paper",
                      width=10,
                      font=("Arial", 11, "bold"),
                      bg="teal",
                      fg="white",
                      command=lambda: game("Paper"))
paper_btn.grid(row=0, column=1, padx=8)


scissor_btn = tk.Button(frame,
                        text="Scissors",
                        width=10,
                        font=("Arial", 11, "bold"),
                        bg="gold",
                        command=lambda: game("Scissors"))
scissor_btn.grid(row=0, column=2, padx=8)


# run the window
root.mainloop()