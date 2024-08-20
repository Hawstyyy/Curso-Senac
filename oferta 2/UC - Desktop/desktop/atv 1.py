from tkinter import *
from tkinter import ttk

root = Tk()

frm = ttk.Frame(root ,padding=50)
frm.grid()
ttk.Label(frm, text="Hello World", ).grid(column=1,row=1)

root.mainloop()