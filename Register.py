""""Register GUI class"""
import Tkinter as Tk

class Register(object):

    """Register GUI class constructor"""
    def __init__(self):

        #Window
        self.root = Tk.Tk()
        self.root.wm_title("Register")

        #Name label
        self.label = Tk.Label(self.root, text="Enter Name")
        self.nameText = Tk.StringVar()
        self.label.pack()
        Tk.Entry(self.root, textvariable=self.nameText).pack()

        #Email label
        self.label = Tk.Label(self.root, text="Enter Email")
        self.emailText = Tk.StringVar()
        self.label.pack()
        Tk.Entry(self.root, textvariable=self.emailText).pack()

        #Set up register button
        self.buttontext = Tk.StringVar()
        self.buttontext.set("Register")
        Tk.Button(self.root, textvariable=self.buttontext, command=self.regClick).pack()

        #Textboxes
        self.nameLabel = Tk.Label(self.root, text="")
        self.emailLabel = Tk.Label(self.root, text="")
        self.nameLabel.pack()
        self.emailLabel.pack()

        #
        self.root.mainloop()


    def regClick(self):
        """Gets the user input"""
        #Need non string exception

        #User input
        #Overrides default input
        name = self.nameText.get()
        email = self.emailText.get()
        self.nameLabel.configure(text=name)
        self.emailLabel.configure(text=email)

        #Test input
        print name
        print email

    def button_click(self):
        """Button click sends to database"""

        #Send to database here
        pass


Register()