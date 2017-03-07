""""Register GUI class"""
import Tkinter as Tk

class Register(object):

    """Register GUI class constructor"""
    def __init__(self):
        #Set up window
        self.root = Tk.Tk()
        self.root.wm_title("Register")

        #Text box label
        self.label = Tk.Label(self.root, text="Enter Name")
        self.label.pack()

        #Set up user input
        self.entrytext = Tk.StringVar()
        Tk.Entry(self.root, textvariable=self.entrytext).pack()

        #Set up register button
        self.buttontext = Tk.StringVar()
        self.buttontext.set("Register")
        Tk.Button(self.root, textvariable=self.buttontext, command=self.regClick).pack()

        #
        self.label = Tk.Label(self.root, text="")
        self.label.pack()

        #
        self.root.mainloop()


    def regClick(self):
        """Gets the user input"""
        #Need non string exception

        #User input
        #Overrides default input
        name = self.entrytext.get()
        self.label.configure(text=name)

        #Test input
        print name

    def button_click(self):
        """Button click sends to database"""

        #Send to database here
        pass


Register()