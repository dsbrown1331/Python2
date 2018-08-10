import tkinter as tk

#create a Tkinter window
window = tk.Tk()

#add code to run when button is pressed
def button_click():
    print("Beep!")

def button2_click():
    print("Honk!")

#create button and put it on the window
button = tk.Button(window, text = "Beep!", command = button_click)
button2 = tk.Button(window, text = "Honk!", command = button2_click)
button.pack()
button2.pack()

#make window appear and handle button presses, etc.
window.mainloop()
