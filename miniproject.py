import tkinter as tk
import random

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")
root.config(bg="#F0F8FF")

result_label = tk.Label(root, text="", font=("Arial", 16), bg="#F0F8FF")
result_label.pack(pady=20)

choices = ['Rock', 'Paper', 'Scissors']

def play(user_choice):
    computer_choice = random.choice(choices)
    
    result_text = f"You chose: {user_choice}\nComputer chose: {computer_choice}\n"
    
    if user_choice == computer_choice:
        result_text += "It's a Tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result_text += "You Win!"
    else:
        result_text += "Computer Wins!"
    
    result_label.config(text=result_text)

btn_frame = tk.Frame(root, bg="#F0F8FF")
btn_frame.pack(pady=30)

rock_btn = tk.Button(btn_frame, text="Rock", width=10, font=("Arial", 12), command=lambda: play('Rock'))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(btn_frame, text="Paper", width=10, font=("Arial", 12), command=lambda: play('Paper'))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(btn_frame, text="Scissors", width=10, font=("Arial", 12), command=lambda: play('Scissors'))
scissors_btn.grid(row=0, column=2, padx=10)

exit_btn = tk.Button(root, text="Exit", command=root.destroy, font=("Arial", 10), bg="#FF6961")
exit_btn.pack(pady=10)

root.mainloop()
