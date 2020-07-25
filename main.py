import tkinter as tk
import sys
from tkinter import *

class MainWindow():
    
    def __init__(self, parent):
        self.parent = parent
        self.parent.geometry("400x400")
        self.frame = tk.Frame(self.parent)
        self.quit_program = tk.Button(self.parent, text='QUIT', command=self.close_main_window).grid()
        self.butnew("Breakfast", Breakfast)
        self.butnew("Lunch", Lunch)
        self.butnew("Dinner", Dinner)
        self.frame.grid()

    def close_main_window(self):
        self.parent.destroy()

    def butnew(self, text, _class):
        tk.Button(self.frame, text=text, command=lambda: self.new_window(_class)).grid()

    def new_window(self, _class):
        self.new = tk.Toplevel(self.parent)
        _class(self.new)
        
    
class Breakfast():

    def __init__(self, parent):
        self.parent = parent 
        self.parent.geometry("400x400")
        self.frame = tk.Frame(self.parent)
        self.entry = tk.Entry(self.frame)
        self.entry_2 = tk.Entry(self.frame)
        self.entry_3 = tk.Entry(self.frame)
        self.label = tk.Label(self.frame, text="What did you eat at breakfast today").grid(row=0, column=0)
        self.label_2 = tk.Label(self.frame, text='Save file as').grid(row=1, column=0)
        self.label_3 = tk.Label(self.frame, text='Date').grid(row=2, column=0)
        self.show = tk.Button(self.frame, text="SHOW", command=self.show_input).grid(row=5, column=1)
        self.quit = tk.Button(self.frame, text="QUIT", command=self.close_window).grid(row=4, column=1)
        self.save = tk.Button(self.frame, text="SAVE", command=self.save_file).grid(row=6, column=1)
        self.entry.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)
        self.entry_3.grid(row=2, column=1)
        self.frame.grid()
    
    def close_window(self):
        self.parent.destroy()

    def show_input(self):
        print(self.entry.get())

    def save_file(self):
        saved_file = self.entry_2.get()
        with open(saved_file, "w") as f:
            f.write(self.entry_3.get() + "\n")
            f.write("Breakfast" + "\n")
            f.write(self.entry.get() + "\n") 

class Lunch():

    def __init__(self, parent):
        self.parent = parent 
        self.parent.geometry("400x400")
        self.frame = tk.Frame(self.parent)
        self.entry = tk.Entry(self.frame)
        self.entry_2 = tk.Entry(self.frame)
        self.entry_3 = tk.Entry(self.frame)
        self.label = tk.Label(self.frame, text="What did you eat at lunch today").grid(row=0, column=0)
        self.label_2 = tk.Label(self.frame, text='Save file as').grid(row=1, column=0)
        self.label_3 = tk.Label(self.frame, text='Date').grid(row=2, column=0)
        self.show = tk.Button(self.frame, text="SHOW", command=self.show_input).grid(row=5, column=1)
        self.quit = tk.Button(self.frame, text="QUIT", command=self.close_window).grid(row=4, column=1)
        self.save = tk.Button(self.frame, text="SAVE", command=self.save_file).grid(row=6, column=1)
        self.entry.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)
        self.entry_3.grid(row=2, column=1)
        self.frame.grid()
    
    def close_window(self):
        self.parent.destroy()

    def show_input(self):
        print(self.entry.get())

    def save_file(self):
        saved_file = self.entry_2.get()
        with open(saved_file, "w") as f:
            f.write(self.entry_3.get() + "\n")
            f.write("Lunch" + "\n")
            f.write(self.entry.get() + "\n") 

class Dinner():

    def __init__(self, parent):
        self.parent = parent 
        self.parent.geometry("400x400")
        self.frame = tk.Frame(self.parent)
        self.entry = tk.Entry(self.frame)
        self.entry_2 = tk.Entry(self.frame)
        self.entry_3 = tk.Entry(self.frame)
        self.label = tk.Label(self.frame, text="What did you eat at lunch today").grid(row=0, column=0)
        self.label_2 = tk.Label(self.frame, text='Save file as').grid(row=1, column=0)
        self.label_3 = tk.Label(self.frame, text='Date').grid(row=2, column=0)
        self.show = tk.Button(self.frame, text="SHOW", command=self.show_input).grid(row=5, column=1)
        self.quit = tk.Button(self.frame, text="QUIT", command=self.close_window).grid(row=4, column=1)
        self.save = tk.Button(self.frame, text="SAVE", command=self.save_file).grid(row=6, column=1)
        self.entry.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)
        self.entry_3.grid(row=2, column=1)
        self.frame.grid()
    
    def close_window(self):
        self.parent.destroy()

    def show_input(self):
        print(self.entry.get())

    def save_file(self):
        saved_file = self.entry_2.get()
        with open(saved_file, "w") as f:
            f.write(self.entry_3.get() + "\n")
            f.write("Dinner" + "\n")
            f.write(self.entry.get() + "\n") 
  

root = tk.Tk()
app = MainWindow(root)
root.mainloop()








           
        
    
        








