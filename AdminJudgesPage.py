import Tkinter as tk   

from BeweeveMain import DATABASE
#
#
#this should more or less be a copy and paste of AdminContestantsPage
#
#
TITLE_FONT = ("Helvetica", 20, "bold")

class AdminJudgesPage(tk.Frame):
    """ Author: Evan Pernu\n
    UW NetID: epernu\n
    Date: 3/11/2017\n
    This is the page that allows admins to view and edit judges"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        backButton = tk.Button(self, text='Back', 
                               command=lambda: controller.show_frame("AdminPage"))

        backButton.pack()