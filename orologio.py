from tkinter import *
import tkinter as tk
import time 
import pyglet


class Orologio():
    cor1 = "#3d3d3d"
    cor2 = "#fafcff"
    cor3 = "#21c25c"
    cor4 = "#eb463b"
    cor5 = "#dedcdc"
    cor6 = "#3080f0"
    cor7 = "#f0f"
    pyglet.font.add_file("digital-7.ttf")
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Orologio")
        self.root.geometry("450x180")
        self.root.configure(bg=self.cor1)
        self.root.resizable(False, False)
        self.orologio = tk.Label(self.root, text="", font=("digital-7", 80), bg=self.cor1, fg=self.cor2)
        self.orologio.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.calendario = tk.Label(self.root, text="", font=("digital-7", 16), bg=self.cor1, fg=self.cor3)
        self.calendario.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.update_orologio()
        

    def update_orologio(self):
        tempo = time.strftime("%H:%M:%S")
        self.orologio.config(text=str(tempo))
        self.calendario.config(text=str(time.strftime("%A, %d %B %Y")))
        self.root.after(200, self.update_orologio)
        #cambio colore se l'orologio è tra le 00:00:00 e le 23:59:00
        if tempo >= "00:00:00" and tempo <= "05:59:59":
            self.orologio.config(fg=self.cor3)
        elif tempo >= "06:00:00" and tempo <= "11:59:59":
            self.orologio.config(fg=self.cor4)
        elif tempo >= "12:00:00" and tempo <= "17:59:59":
            self.orologio.config(fg=self.cor7)
        elif tempo >= "18:00:00" and tempo <= "23:59:59":
            self.orologio.config(fg=self.cor6)
        else:
            self.orologio.config(fg=self.cor2)
            
    #mainloop
    def mainloop(self):
        self.root.mainloop()
            
if __name__ == "__main__":
    app = Orologio()
    app.mainloop()
    
    