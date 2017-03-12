import Tkinter as tk   

from Database import *

#DATABASE = Database()

TITLE_FONT = ("Helvetica", 20, "bold")

class RegistrationPage(tk.Frame):
    """Author: Thomas Schmidt\n
    Date: 3/5/2017\n
    Author: Evan Pernu\n
    UW NetID: epernu\n
    Date: 3/11/2017\n
    This is the RegistrationPage Class that will show the registration page once the user attempts to register."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.label = tk.Label(self, text="Registration", font=TITLE_FONT)
        self.label.pack(side="top", fill="x", pady=10)

        self.label_1 = tk.Label(self, text="Full Name")
        self.nameText = tk.StringVar()
        self.label_1.pack(side="top")
        tk.Entry(self, textvariable=self.nameText).pack()

        self.label_2 = tk.Label(self, text="Email")
        self.emailText = tk.StringVar()
        self.label_2.pack(side="top")
        tk.Entry(self, textvariable=self.emailText).pack()

        button = tk.Button(self, text="Submit",
                           command=self.regClick)
        button.pack()

        backButton = tk.Button(self, text='Back', 
                               command=lambda: controller.show_frame("LoginPage"))
        backButton.pack()

    def regClick(self):
        """Gets the user input"""
        #Need non string exception

        #User input
        #Overrides default input
        name = self.nameText.get()
        email = self.emailText.get()

        global DATABASE 
        DATABASE = Database()
        userID = self.sendToDatabase(name, email)    #added by Alex Lambert 3/9/17
        DATABASE.commit()                            #added by Alex Lambert 3/9/17
        DATABASE.closeDB()        

        self.displayUserID(userID)
        #Test input
        # print name
        # print email

    def sendToDatabase(self, name, email):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/9/17\n
            Add contestant to the Database"""

        entry = [name, email, '']
        return  DATABASE.addContestant(entry)

    def displayUserID(self, userID):
        userID = tk.Label(self, text=userID)
        userID.pack()