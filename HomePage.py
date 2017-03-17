import Tkinter as tk   

from BeweeveMain import DATABASE, CURRENT_USER

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
        #self.update()

        label = tk.Label(self, text="Welcome!", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        #str = 

        idLabel = tk.Label(self, text="ID: %i" %(CURRENT_USER.userID))
        idLabel.pack()

        
        button2 = tk.Button(self, text = "Event Schedule", width=12, command=lambda: controller.show_frame("EventSchedulePage")) 
        button4 = tk.Button(self, text = "Judges", width=12, command=lambda: controller.show_frame("JudgesPage"))


        button4.pack(pady=5)
        button2.pack(pady=5)
    

        button = tk.Button(self, text="Logout", width=12,
                           command=lambda: controller.show_frame("LoginPage"))
        button.pack()

