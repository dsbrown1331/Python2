import tkinter as tk
import piglatin

window = tk.Tk()

def translate_word():
    entered_word = word_entry.get()
    translation = piglatin.convert_to_piglatin(entered_word)
    translation_label.config(text = translation)

word_label = tk.Label(window, text = "English word:")
word_entry = tk.Entry(window)

button = tk.Button(window, text="Translate to Piglatin", command=translate_word)
translation_label = tk.Label(window)

word_label.pack()
word_entry.pack()
button.pack()
translation_label.pack()

window.mainloop()
