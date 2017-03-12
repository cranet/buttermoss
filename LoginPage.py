import Tkinter as tk   

from BeweeveMain import DATABASE

TITLE_FONT = ("Helvetica", 20, "bold")

class LoginPage(tk.Frame):
    """Author: Thomas Schmidt\n
    Date: 3/5/2017\n
    Author: Evan Pernu\n
    UW NetID: epernu\n
    Date: 3/11/2017\n
    This is the LoginPage Class that will pop up upon startup."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="BeWeeve", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        label_1 = tk.Label(self, text="User ID")
        label_1.pack(side="top")

        self.entry_1 = tk.Entry(self)
        self.entry_1.pack(side="top")

        button = tk.Button(self, text='Login', command=lambda: self.reg_Click())
        button.pack()

        button_2 = tk.Button(self, text="Register",
                            command=lambda: self.reg_Page())
        button_2.pack()

    def reg_Click(self):
        """check login credentials"""
        #Need non string exception

        #User input
        #Overrides default input
        userID = self.entry_1.get()

        if DATABASE.doesUserExist(userID):
            self.controller.show_frame('HomePage')
        else:
            label = tk.Label(self, text='FAILURE!')
            label.pack()

    def reg_Page(self):
        """Bring up registration page"""
        self.controller.show_frame("RegistrationPage")
