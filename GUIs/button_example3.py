import tkinter as tk

#create a Tkinter window
window = tk.Tk()

count = 0

#add code to run when button is pressed
def button_click():
    global count
    count += 1
    button.config(text = str(count))

#create button and put it on the window
button = tk.Button(window, text = "Click me!", command = button_click)
button.pack()

#make window appear and handle button presses, etc.
window.mainloop()
