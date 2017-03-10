# Created by Thomas Schmidt 3/5/2017
# This simple program creates the basic GUI for the BeweeveApp

import Tkinter as tk   

from Database import *

DATABASE = Database() #added by Alex Lambert 3/9/17

TITLE_FONT = ("Helvetica", 20, "bold")

class BeweeveApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # This container stacks a bunch of frames on top of each other. 
        # The one we want visible will be raised above the others.
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.title("Beweeve")
        self.frames = {}
        
        for F in (LoginPage, HomePage, RegistrationPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # This puts all of the pages in the same location.
            # The one on the top of the stacking order will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

# This is the LoginPage Class that will pop up upon startup.
class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="BeWeeve", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        label_1 = tk.Label(self, text="User ID")
        label_1.pack(side="top")

        self.entry_1 = tk.Entry(self)
        self.entry_1.pack(side="top")

        # label_2 = tk.Label(self, text="Password")
        # label_2.pack(side="top")

        # entry_2 = tk.Entry(self)
        # entry_2.pack(side="top")


        # button_1 = tk.Button(self, text="Login",
        #                     command=self.regClick())

        button = tk.Button(self, text='Login', command=lambda: controller.show_frame("RegistrationPage"))
        button.pack()

        button_2 = tk.Button(self, text="Register",
                            command=lambda: controller.show_frame("RegistrationPage"))
        button_2.pack()

    def regClick(self):
        """check login credentials"""
        #Need non string exception

        #User input
        #Overrides default input
        userID = self.entry_1.get()

        if DATABASE.doesUserExist(userID):
            print 'succes'
            label = tk.Label(self, text='SUCCESS!')
            label.pack()
        # else:
        #     label = tk.Label(self, text='FAILURE!')
        #     label.pack()

# This is the HomePage Class that will show the home page screen once the user has logged in.
class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="This is home page once logged in!", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Logout",
                           command=lambda: controller.show_frame("LoginPage"))
        button.pack()

# This is the RegistrationPage Class that will show the registration page once the user attempts to register.
class RegistrationPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.label = tk.Label(self, text="Registration", font=TITLE_FONT)
        self.label.pack(side="top", fill="x", pady=10)

        self.label_1 = tk.Label(self, text="Full Name")
        self.nameText = tk.StringVar()
        self.label_1.pack(side="top")
        tk.Entry(self, textvariable=self.nameText).pack()

        # entry_1 = tk.Entry(self)
        # entry_1.pack(side="top")

        self.label_2 = tk.Label(self, text="Email")
        self.emailText = tk.StringVar()
        self.label_2.pack(side="top")
        tk.Entry(self, textvariable=self.emailText).pack()
        # entry_2 = tk.Entry(self)
        # entry_2.pack(side="top")

        # label_3 = tk.Label(self, text="Desired Username")
        # label_3.pack(side="top")

        # entry_3 = tk.Entry(self)
        # entry_3.pack(side="top")

        # label_4 = tk.Label(self, text="Desired Password")
        # label_4.pack(side="top")

        # entry_4 = tk.Entry(self)
        # entry_4.pack(side="top")

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

        userID = self.sendToDatabase(name, email)    #added by Alex Lambert 3/9/17
        DATABASE.commit()                            #added by Alex Lambert 3/9/17
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
# This is the loop to keep application running.
if __name__ == "__main__":
    app = BeweeveApp()
    app.mainloop()