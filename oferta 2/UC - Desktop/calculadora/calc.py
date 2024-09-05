import customtkinter
from tkinter import messagebox
from tkinter import StringVar
expressao = ''

class App():
  def __init__(self) -> None:
    pass

  def botao(self, main,text,height,row,column,x,y, command):
    button = customtkinter.CTkButton(main, text=text, height=height, command = command)
    button.grid(row = row, column = column, padx = x, pady = y,)

  def calc(self, entry):
    expressao = entry.get()
    res = eval(expressao)
    entry.delete('0','end')
    entry.insert("0", res)

  def start_app(self):
    global entry
    app = customtkinter.CTk()
    app.title("Calculadora")
    app.geometry("400x500")
    app.resizable(False, False)

    app.grid_columnconfigure(0, weight=1)
    app.grid_columnconfigure(1, weight=1)
    app.grid_columnconfigure(2, weight=1)

    entry = customtkinter.CTkEntry(app, fg_color="white", height=50, width=360, text_color="black", font=customtkinter.CTkFont(family='arial', size=32))
    entry.grid(row = 0, columnspan=4, pady=20, padx=20)
  
    self.botao(app, "1", 50, 1, 0, 10, 15, lambda: entry.insert('end',"1"))
    self.botao(app, "2", 50, 1, 1, 10, 15, lambda: entry.insert('end',"2"))
    self.botao(app, "3", 50, 1, 2, 10, 15, lambda: entry.insert('end',"3"))
    self.botao(app, "4", 50, 2, 0, 10, 15, lambda: entry.insert('end',"4"))
    self.botao(app, "5", 50, 2, 1, 10, 15, lambda: entry.insert('end',"5"))
    self.botao(app, "6", 50, 2, 2, 10, 15, lambda: entry.insert('end',"6"))
    self.botao(app, "7", 50, 3, 0, 10, 15, lambda: entry.insert('end',"7"))
    self.botao(app, "8", 50, 3, 1, 10, 15, lambda: entry.insert('end',"8"))
    self.botao(app, "9", 50, 3, 2, 10, 15, lambda: entry.insert('end',"9"))
    self.botao(app, "0", 50, 4, 1, 10, 15, lambda: entry.insert('end',"0"))
    self.botao(app, "+", 50, 4, 0, 10, 15, lambda: entry.insert('end',"+"))
    self.botao(app, "-", 50, 4, 2, 10, 15, lambda: entry.insert('end',"-"))

    self.botao(app, "C", 50, 1, 3, 10, 15, lambda: entry.delete('0', 'end'))
    self.botao(app, "/", 50, 2, 3, 10, 15, lambda: entry.insert('end',"/"))
    self.botao(app, "*", 50, 3, 3, 10, 15, lambda: entry.insert('end',"*"))
    self.botao(app, "(1/2)", 50, 5, 3, 10, 15, lambda: entry.insert('end',"/(1/2)"))
    self.botao(app, "=", 50, 4, 3, 10, 15, lambda: self.calc(entry))

    app.mainloop()

if __name__ == "__main__":
  App().start_app()