import random
import tkinter as tk
window = tk.Tk()

max_num = 10
score = 0
rounds = 0

def button_click():
    global score
    global rounds

    try:
        guess = int(guess_box.get())
        if 0 <= guess <= max_num:
            result = random.randint(0,max_num)
            if guess == result:
                #correct guess so increment score
                score += 1
            else:
                #just increment number of rounds
                rounds += 1
        else:
            result = "Not a valid guess!"
    except:
        result = "Not a valid guess!"

    result_label.config(text = result)
    score_label.config(text = str(score) + "/" + str(rounds))
    guess_box.delete(0, tk.END)

guess_label = tk.Label(window, text = "Enter a number between 0 and " + str(max_num))
guess_box = tk.Entry(window)
result_label = tk.Label(window)
score_label = tk.Label(window)
button = tk.Button(window, text = "Guess", command = button_click)

guess_label.pack()
guess_box.pack()
result_label.pack()
score_label.pack()
button.pack()
window.mainloop()
