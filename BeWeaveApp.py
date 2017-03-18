"""Beweeve App"""
import Tkinter as tk
from LoginPage import LoginPage
from HomePage import HomePage
from RegistrationPage import RegistrationPage
from JudgesPage import JudgesPage
from EventSchedulePage import EventSchedulePage
from AdminJudgesPage import AdminJudgesPage
from AdminCategoriesPage import AdminCategoriesPage
from AdminContestantsPage import AdminContestantsPage
from AdminPage import AdminPage

class BeWeaveApp(tk.Tk):
    """Author: Thomas Schmidt\n
    Date: 3/5/2017\n
    Author: Evan Pernu\n
    UW NetID: epernu\n
    Date: 3/14/2017\n
    This is the main app that controls each frame."""

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #This container stacks a bunch of frames on top of each other
        #The one we want visible will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.title("BeWeeve")
        self.frames = {}
        self.frames["LoginPage"] = LoginPage(parent=container, controller=self)
        self.frames["HomePage"] = HomePage(parent=container, controller=self)
        self.frames["RegistrationPage"] = RegistrationPage(parent=container, controller=self)
        self.frames["JudgesPage"] = JudgesPage(parent=container, controller=self)
        self.frames["EventSchedulePage"] = EventSchedulePage(parent=container, controller=self)
        self.frames["AdminPage"] = AdminPage(parent=container, controller=self)
        self.frames["AdminJudgesPage"] = AdminJudgesPage(parent=container, controller=self)
        self.frames["AdminCategoriesPage"] = AdminCategoriesPage(parent=container, controller=self)
        self.frames["AdminContestantsPage"] = AdminContestantsPage(parent=container,
                                                                   controller=self)

        self.frames["LoginPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["HomePage"].grid(row=0, column=0, sticky="nsew")
        self.frames["RegistrationPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["JudgesPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["EventSchedulePage"].grid(row=0, column=0, sticky="nsew")
        self.frames["AdminPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["AdminJudgesPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["AdminCategoriesPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["AdminContestantsPage"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()
