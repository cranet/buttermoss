import Tkinter as tk   

from BeweeveMain import DATABASE, CURRENT_USER

TITLE_FONT = ("Helvetica", 20, "bold")

class LoginPage(tk.Frame):
    """Author: Thomas Schmidt\n
    Date: 3/5/2017\n
    Author: Evan Pernu\n
    UW NetID: epernu\n
    Date: 3/14/2017\n
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

        button = tk.Button(self, text='Login', width="10", command=lambda: self.reg_Click())
        button.pack(pady=5)

        button_2 = tk.Button(self, text="Register", width="10",
                             command=lambda: self.reg_Page())
        button_2.pack()





        

    def reg_Click(self):
        """check login credentials"""
        #Need non string exception

        #User input
        #Overrides default input
        if self.entry_1.get() != "":
            userID = self.entry_1.get()

            log = DATABASE.doesUserExist(userID)
            if log == 1:
                self.controller.show_frame('HomePage')
            elif log == 3:
                self.controller.show_frame('AdminPage')
            elif log == 2:
                self.controller.show_frame('HomePage')  #if the user is a judge
            else:
                self.error("FAILURE")

        else:
            self.error("PLEASE ENTER TEXT")
            #controller.show_frame("RegistrationPage")

    def reg_Page(self):
        """Bring up registration page"""
        self.controller.show_frame("RegistrationPage")
    
    def error(self, string):
        self.errorPop = tk.Tk()
        self.errorPop.wm_title("ERROR")
        self.errorLabel = tk.Label(self.errorPop, text=string)
        self.errorLabel.pack()
        self.errorButton = tk.Button(self.errorPop, text="Okay", command=self.errorPop.destroy)
        self.errorButton.pack(pady=5)
