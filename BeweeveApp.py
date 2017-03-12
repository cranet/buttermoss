
import Tkinter as tk   

from Database import *
from LoginPage import *
from HomePage import *
from registerContestPage import *
from RegistrationPage import *

#DATABASE = Database() #added by Alex Lambert 3/9/17

TITLE_FONT = ("Helvetica", 20, "bold")

class BeweeveApp(tk.Tk):
    """Author: Thomas Schmidt\n
    Date: 3/5/2017\n
    Author: Evan Pernu\n
    UW NetID: epernu\n
    Date: 3/11/2017\n
    This is the main app that controls each frame."""

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # This container stacks a bunch of frames on top of each other. 
        # The one we want visible will be raised above the others.
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.title("BeWeeve")
        self.frames = {}
        
       # for F in (LoginPage, HomePage, RegistrationPage, registerContestPage):
        #    page_name = F.__name__
         #   frame = F(parent=container, controller=self)
          #  self.frames[page_name] = frame

            # This puts all of the pages in the same location.
            # The one on the top of the stacking order will be the one that is visible.
           # frame.grid(row=0, column=0, sticky="nsew")
        
        self.frames["LoginPage"] = LoginPage(parent=container, controller=self)
        self.frames["HomePage"] = HomePage(parent=container, controller=self)
        self.frames["RegistrationPage"] = RegistrationPage(parent=container, controller=self)
        self.frames["registerContestPage"] = registerContestPage(parent=container, controller=self)

        self.frames["LoginPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["HomePage"].grid(row=0, column=0, sticky="nsew")
        self.frames["RegistrationPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["registerContestPage"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()



# This is the loop to keep application running.
if __name__ == "__main__":
    app = BeweeveApp()
    app.mainloop()
