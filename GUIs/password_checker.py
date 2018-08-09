import tkinter as tk
window = tk.Tk()

def check_password():
    password = "Banana"
    entered_password = password_entry.get()
    if password == entered_password:
        confirm_label.config(text = "Correct")
    else:
        confirm_label.config(text = "Incorrect")

password_label = tk.Label(window, text = "Password")
password_entry = tk.Entry(window, show="*")

button = tk.Button(window, text="Enter", command=check_password)
confirm_label = tk.Label(window)

password_label.pack()
password_entry.pack()
button.pack()
confirm_label.pack()

window.mainloop()
