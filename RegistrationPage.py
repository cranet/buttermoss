import Tkinter as tk   

from BeweeveMain import DATABASE, CURRENT_USER

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
                           command=lambda: self.regClick(controller))
        button.pack()

        backButton = tk.Button(self, text='Back', 
                               command=lambda: controller.show_frame("HomePage"))
        
        backButton.pack()

    def regClick(self, controller):
        
        #Need non string exception
        if self.nameText.get() != "" or self.emailText.get() != "":

            #User input
            #Overrides default input
            name = self.nameText.get()
            email = self.emailText.get()

            global DATABASE 
            CURRENT_USER.userID = self.sendToDatabase(name, email)    #added by Alex Lambert 3/9/17
            DATABASE.commit()                            #added by Alex Lambert 3/9/17  

            self.pop = tk.Tk()
            self.pop.wm_title("User ID")
            label = tk.Label(self.pop, text=CURRENT_USER.userID)
            label.pack(fill="x", pady=10)
            button = tk.Button(self.pop, text="Okay", command=lambda: self.daisy())
            button.pack()

            #self.displayUserID(CURRENT_USER.userID)
            #CURRENT_USER.userID = userID
            #Test input
            # print name
            # print email
        else:
            self.errorPop = tk.Tk()
            self.errorPop.wm_title("ERROR")
            self.errorLabel = tk.Label(self.errorPop, text="PLEASE ENTER TEXT")
            self.errorLabel.pack()
            self.errorButton = tk.Button(self.errorPop, text="Okay", command=self.errorPop.destroy)
            self.errorButton.pack(pady=5)
            #controller.show_frame("RegistrationPage")

    def daisy(self):
        print "stupid"
        self.pop.destroy()
        self.controller.show_frame("HomePage")
        

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