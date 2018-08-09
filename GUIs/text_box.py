import tkinter as tk
window = tk.Tk()

def change_string():
    string_to_copy = entry.get()
    string_to_copy = string_to_copy[::-1]
    entry.delete(0, tk.END)
    entry.insert(0, string_to_copy)

entry = tk.Entry(window)
button = tk.Button(window, text="Reverse", command = change_string)

entry.pack()
button.pack()
window.mainloop()
