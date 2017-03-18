"""Admin Page"""
import Tkinter as tk

class AdminPage(tk.Frame):
    """ Author: Evan Pernu\n
    UW NetID: epernu\n
    Date: 3/11/2017\n
    This is the home page for admins."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        button = tk.Button(self, text='Judges', width=12,
                           command=lambda: controller.show_frame("AdminJudgesPage"))
        button2 = tk.Button(self, text='Categories', width=12,
                            command=lambda: controller.show_frame("AdminCategoriesPage"))
        button3 = tk.Button(self, text='Contestants', width=12,
                            command=lambda: controller.show_frame("AdminContestantsPage"))
        backButton = tk.Button(self, text='Logout', width=12,
                               command=lambda: controller.show_frame("LoginPage"))

        button.pack(pady=5)
        button2.pack(pady=5)
        button3.pack(pady=5)
        backButton.pack(pady=5)
