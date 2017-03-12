import Tkinter as tk   

from BeweeveMain import DATABASE

TITLE_FONT = ("Helvetica", 20, "bold")


class HomePage(tk.Frame):
    """Author: Thomas Schmidt\n
    Date: 3/5/2017\n
    Author: Evan Pernu\n
    UW NetID: epernu\n
    Date: 3/11/2017\n
    This is the HomePage Class that will show the home page screen once the user has logged in."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="This is home page once logged in!", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        
        button2 = tk.Button(self, text = "Event Schedule") 
        button3 = tk.Button(self, text = "Register for Contest", command=lambda: controller.show_frame("registerContestPage"))
        button4 = tk.Button(self, text = "Judges")

        button3.pack()
        button4.pack()
        button2.pack()
    

        button = tk.Button(self, text="Logout",
                           command=lambda: controller.show_frame("LoginPage"))
        button.pack()