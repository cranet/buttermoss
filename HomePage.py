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
        print DATABASE.getAllContestantUserIDs()
        idLabel = tk.Label(self, text="ID: %i" %(CURRENT_USER.userID))
        idLabel.pack()
        print CURRENT_USER.userID
        print CURRENT_USER.email
        
        button2 = tk.Button(self, text = "Event Schedule", command=lambda: controller.show_frame("EventSchedulePage")) 
        button3 = tk.Button(self, text = "Register for Contest", command=lambda: controller.show_frame("registerContestPage"))
        button4 = tk.Button(self, text = "Judges", command=lambda: controller.show_frame("JudgesPage"))

        idButton = tk.Button(self, text="Show ID", command=self.showID)

        button3.pack()
        button4.pack()
        button2.pack()
        idButton.pack()
    

        button = tk.Button(self, text="Logout",
                           command=lambda: controller.show_frame("LoginPage"))
        button.pack()

    def showID(self):
        pop = tk.Tk()
        pop.wm_title("User ID")
        label = tk.Label(pop, text=CURRENT_USER.userID)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(pop, text="Close", command=pop.destroy)
        button.pack()

