from schedule import every, run_pending
from time import sleep
from os.path import dirname
import tkinter as tk

def reminder():

    def exitprog():
        window.destroy()

    window = tk.Tk()
    window.title("Drink Water!")
    window.iconbitmap(dirname(__file__) + "\\icon.ico")
    frame = tk.Frame(master=window, padx=100, borderwidth=10)
    frame.pack()
    message = tk.Label(master=frame, text="Drink water!\n")
    message.pack()
    exitbutton = tk.Button(master=frame, text="Exit", padx=20, command=lambda:exitprog())
    exitbutton.pack()
    window.mainloop()

every(1).hour.do(reminder)

while True:
    run_pending()
    sleep(1)