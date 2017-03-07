from Tkinter import *
import tkMessageBox

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
        #User input
        input
        self.label.configure(texdt=input)

    def button_click(self, e):
        pass



Register()