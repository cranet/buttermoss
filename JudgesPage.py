import Tkinter as tk   

from BeweeveMain import DATABASE

TITLE_FONT = ("Helvetica", 20, "bold")

class JudgesPage(tk.Frame):
    """ Author: Evan Pernu\n
    UW NetID: epernu\n
    Date: 3/11/2017\n
    This page displays a list of judges"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        backButton = tk.Button(self, text='Back', 
                               command=lambda: controller.show_frame("HomePage"))
                               
        backButton.pack()
