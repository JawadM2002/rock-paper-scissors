import random 
import tkinter as tk
from tkinter import ttk

class RockPaperScissors:
    
    def __init__(self): # Creation of GUI
        self.window = tk.Tk()
        self.window.title("Rock Paper Scissors")
        self.window.geometry("1280x720")
        self.window.resizable(False, False)
        self.window.config(bg="#ADD8E6")

        self.rock_icon = tk.PhotoImage(file="rock.png")
        self.window.iconphoto(True, self.rock_icon)
        self.rock_icon = self.rock_icon.subsample(1, 1)

        # results of both the user and the computer
        self.user_score = 0
        self.computer_score = 0
        self.results = []

        self.label = tk.Label(self.window, text="Select rock, paper or scissors: ", 
                              font=("Times New Roman", 20, "bold"), fg="blue", bg="#ADD8E6")
        self.label.pack(pady=20)

        self.entry = tk.Entry(self.window, font=("Arial", 12))
        self.entry.pack(fill="x", pady=40)

        self.button = tk.Button(self.window, text="Play", 
                                font=("Times New Roman", 20, "bold"), command=self.play, bg="#F7DC6F")
        self.button.pack(pady=20)

        self.reset_button = tk.Button(self.window, text="Reset", 
                                      font=("Times New Roman", 20, "bold"), bg="firebrick", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, pady=10)

        self.stats_button = tk.Button(self.window, text="Stats", 
                                      font=("Times New Roman", 20, "bold"), bg="orange", command=self.stats)
        self.stats_button.pack(side=tk.LEFT, pady=20)

        self.result_label = tk.Label(self.window, text="", fg="crimson", bg="#ADD8E6")
        self.result_label.pack(fill="x",pady=20)

        self.score_label = tk.Label(self.window, text=f"Score - You: {self.user_score}, Computer: {self.computer_score}", 
                                    font=("Arial", 20, "bold"), fg="navy", bg="#ADD8E6")
        self.score_label.pack()

        # Creates a table that determines the result of each round
        self.tree = ttk.Treeview(self.window, columns=('User', 'Computer', 'Outcome'))
        self.tree.column('User', width=300, anchor='center')
        self.tree.column('Computer', width=300, anchor='center')
        self.tree.column('Outcome', width=300, anchor='center')
        self.tree.heading('User', text='User')
        self.tree.heading('Computer', text='Computer')
        self.tree.heading('Outcome', text='Outcome')
        self.tree.pack(padx=25, pady=25, expand=True)

        self.window.mainloop()

    def play(self):
        user_choice = self.entry.get().lower()
         # If the user chooses to quit
        if user_choice == 'quit':
            self.window.quit()
            return
        
        # If the user chooses a different choice outside the default choice
        if user_choice not in ["rock", "paper", "scissors"]:
            self.result_label.config(text="Invalid choice, please try again")
            return
        # The random choices to choose from
        computer_choice = random.choice(["rock", "paper", "scissors"])
        
        if computer_choice == user_choice: # If user and computer have same result
            result = "It's a tie!"
        elif ((user_choice=="paper" and computer_choice=="scissors") or 
              (user_choice=="rock" and computer_choice=="paper") or 
              (user_choice=="scissors" and computer_choice=="rock")): # User loses, computer wins
            result = "You lose!"
            self.computer_score += 1
        elif ((user_choice=="scissors" and computer_choice=="paper") or 
              (user_choice=="rock" and computer_choice=="scissors") or
              (user_choice=="paper" and computer_choice=="rock")): # user wins, computer loses
            result = "You win!"
            self.user_score += 1

        # Manages the scores of the user and computer
        self.result_label.config(text=f"User: {user_choice}, Computer: {computer_choice}")
        self.score_label.config(text=f"Score - You: {self.user_score}, Computer: {self.computer_score}")
        self.entry.delete(0, tk.END)

        self.results.append((user_choice, computer_choice, result))
        self.tree.insert('', 'end', values=(user_choice, computer_choice, result)) # adds results on table

        if len(self.results) > 10: # returns up to 10 results
            self.tree.delete(0)
            self.results = self.results[-10:]
    
    def reset(self):
        self.user_score = 0
        self.computer_score = 0
        self.results = []
        self.tree.delete(*self.tree.get_children())
        self.score_label.config(text=f"Score - You: {self.user_score}, Computer: {self.computer_score}")
    
    def stats(self):
        wins = [r[2] for r in self.results if r[2] == "You win!"]
        losses = [r[2] for r in self.results if r[2] == "You lose!"]
        ties = [r[2] for r in self.results if r[2] == "It's a tie!"]

        stats_window = tk.Tk()
        stats_window.title("Stats of Rock Paper Scissors")
        stats_window.geometry("400x300")
        stats_window.resizable(False, False)

        tk.Label(stats_window, text=f"Wins: {len(wins)}", font=("Arial", 16)).pack()
        tk.Label(stats_window, text=f"Losses: {len(losses)}", font=("Arial", 16)).pack()
        tk.Label(stats_window, text=f"Ties: {len(ties)}", font=("Arial", 16)).pack()

        stats_window.mainloop()  

if __name__ == "__main__":
    game = RockPaperScissors()