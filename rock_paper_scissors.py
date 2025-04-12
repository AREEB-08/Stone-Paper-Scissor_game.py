import tkinter as tk
import random

# Weapons and emojis
weapons = {'stone': '✊', 'paper': '✋', 'scissors': '✌'}
choices = list(weapons.keys())

class RPSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        self.root.geometry("400x600")
        self.root.config(bg='#34495E')

        self.create_widgets()

    def create_widgets(self):
        # Game Title
        title = tk.Label(self.root, text="Rock Paper Scissors", font=("Verdana", 22, 'bold'),
                         fg="#F1C40F", bg="#34495E")
        title.pack(pady=(20, 10))

        # User Label
        tk.Label(self.root, text="Choose Your Weapon", font=("Helvetica", 16),
                 fg='white', bg='#34495E').pack(pady=(10, 10))

        # User Choices
        self.choice_frame = tk.Frame(self.root, bg='#34495E')
        self.choice_frame.pack(pady=10)

        for key, symbol in weapons.items():
            tk.Button(self.choice_frame, text=symbol, font=("Helvetica", 28), width=4,
                      bg='#1ABC9C', fg='white', activebackground='#16A085',
                      command=lambda k=key: self.play(k)).pack(side=tk.LEFT, padx=10)

        # VS Display
        self.fight_label = tk.Label(self.root, text="❔  VS  ❔", font=("Helvetica", 40, "bold"),
                                    fg="#ECF0F1", bg="#34495E")
        self.fight_label.pack(pady=(30, 10))

        # Result Label
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 18, "bold"),
                                     bg='#34495E', fg='#F39C12')
        self.result_label.pack(pady=(10, 10))

        # Computer's Choice Display
        self.comp_label = tk.Label(self.root, text="Computer chose: ❔", font=("Helvetica", 14),
                                   fg='white', bg='#34495E')
        self.comp_label.pack(pady=(5, 5))

        # Play Again Button (initially hidden)
        self.play_again_btn = tk.Button(self.root, text="Play Again", font=("Helvetica", 14, "bold"),
                                        bg="#E74C3C", fg='white', activebackground='#C0392B',
                                        command=self.reset)
        # Note: It will be packed only after the first round

    def play(self, user_choice):
        computer_choice = random.choice(choices)

        # Update UI with choices
        self.fight_label.config(text=f"{weapons[user_choice]}  VS  {weapons[computer_choice]}")
        self.comp_label.config(text=f"Computer chose: {weapons[computer_choice]} ({computer_choice})")

        # Determine result
        if user_choice == computer_choice:
            result = "It's a draw!"
        elif (user_choice == 'stone' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'stone') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            result = "You Win! 🎉"
        else:
            result = "Computer Wins! 💻"

        self.result_label.config(text=result)

        # Disable weapon buttons after play
        for widget in self.choice_frame.winfo_children():
            widget.config(state=tk.DISABLED)

        # Show Play Again Button
        self.play_again_btn.pack(pady=(20, 10))

    def reset(self):
        # Reset all labels
        self.fight_label.config(text="❔  VS  ❔")
        self.result_label.config(text="")
        self.comp_label.config(text="Computer chose: ❔")

        # Enable buttons
        for widget in self.choice_frame.winfo_children():
            widget.config(state=tk.NORMAL)

        # Hide Play Again Button
        self.play_again_btn.pack_forget()

if __name__ == '__main__':
    root = tk.Tk()
    app = RPSGame(root)
    root.mainloop()
