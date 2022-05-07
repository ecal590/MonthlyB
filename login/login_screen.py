from tkinter import *
from tkinter import ttk

root = Tk()
form = ttk.Frame(root, padding= 10)
form.grid()
ttk.Label(form, text="Location").grid(column=0, row=0)
ttk.Button(form, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
