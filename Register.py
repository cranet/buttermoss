""""Imports"""
from Tkinter import Label
from Tkinter import Entry
from Tkinter import StringVar
from Tkinter import Button
from Tkinter import Tk

import tkMessageBox

"""Register GUI class"""
class Register(object):

    def __init__(self):
        
        #Set up window
        self.root = Tk()
        self.root.wm_title("Register")

        #Text box label
        self.label = Label(self.root, text="Enter Name")
        self.label.pack()

        #Set up user input
        self.entrytext = StringVar()
        Entry(self.root, textvariable=self.entrytext).pack()

        #Set up register button
        self.buttontext = StringVar()
        self.buttontext.set("Register")
        Button(self.root, textvariable=self.buttontext, command=self.regClick).pack()

        #
        self.label = Label(self.root, text="")
        self.label.pack()

        #
        self.root.mainloop()

    
    def regClick(self):
        
        #Need non string exception

        #User input
        input = self.entrytext.get()
        self.label.configure(text=input)
        
        #Test 
        print input

    def button_click(self, e):
        #Send to database here
        pass


Register()