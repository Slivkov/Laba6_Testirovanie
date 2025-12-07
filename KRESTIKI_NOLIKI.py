import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Krestik-Nolik")
        
        self.cells = [''] * 9
        self.buttons = []
        
        for i in range(9):
            btn = tk.Button(self.root, text='', font=('Arial', 40), 
                          width=3, height=1,
                          command=lambda i=i: self.click(i))
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)
    
    def click(self, i):
        if self.cells[i] or hasattr(self, 'finished'):
            return
        
        self.cells[i] = 'X'
        self.buttons[i].config(text='X', fg='blue')
        
        if self.win_check('X'):
            self.end("Pobeda!")
            return
        
        if all(self.cells):
            self.end("Nichya!")
            return
        
        self.root.after(300, self.computer)
    
    def computer(self):
        empty = [i for i,v in enumerate(self.cells) if not v]
        if not empty:
            return
        
        for i in empty:
            self.cells[i] = 'O'
            if self.win_check('O'):
                self.buttons[i].config(text='O', fg='red')
                self.end("Potracheno!")
                return
            self.cells[i] = ''
        
        for i in empty:
            self.cells[i] = 'X'
            if self.win_check('X'):
                self.cells[i] = 'O'
                self.buttons[i].config(text='O', fg='red')
                return
            self.cells[i] = ''
        
        i = random.choice(empty)
        self.cells[i] = 'O'
        self.buttons[i].config(text='O', fg='red')
        
        if self.win_check('O'):
            self.end("Potracheno!")
            return
        
        if all(self.cells):
            self.end("Nikto!")
    
    def win_check(self, player):
        lines = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]
        for line in lines:
            if all(self.cells[i] == player for i in line):
                for i in line:
                    self.buttons[i].config(bg='yellow')
                return True
        return False
    
    def end(self, msg):
        self.finished = True
        messagebox.showinfo("Potracheno!", msg)
        self.root.after(2000, self.root.destroy)
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    TicTacToe().run()