import Tkinter as tk   

from BeweeveMain import DATABASE, CURRENT_USER

TITLE_FONT = ("Helvetica", 20, "bold")

class AdminPage(tk.Frame):
    """ Author: Evan Pernu\n
    UW NetID: epernu\n
    Date: 3/11/2017\n
    This is the home page for admins."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        button = tk.Button(self, text='Judges', 
                               command=lambda: controller.show_frame("AdminJudgesPage"))
        button2 = tk.Button(self, text='Categories', 
                               command=lambda: controller.show_frame("AdminCategoriesPage"))
        button3 = tk.Button(self, text='Contestants', 
                               command=lambda: controller.show_frame("AdminContestantsPage"))
        backButton = tk.Button(self, text='Back', 
                               command=lambda: controller.show_frame("HomePage"))

        button.pack()
        button2.pack()
        button3.pack()
        backButton.pack()
