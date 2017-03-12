# Created by Thomas Schmidt 3/5/2017
# This simple program creates the basic GUI for the BeweeveApp

import Tkinter as tk   


TITLE_FONT = ("Helvetica", 20, "bold")

class BeweeveApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # This container stacks a bunch of frames on top of each other. 
        # The one we want visible will be raised above the others.
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.title("Beweeve")
        self.frames = {}
        
        for F in (LoginPage, HomePage, RegistrationPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # This puts all of the pages in the same location.
            # The one on the top of the stacking order will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

# This is the LoginPage Class that will pop up upon startup.
class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Beweeve", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        label_1 = tk.Label(self, text="Username")
        label_1.pack(side="top")

        entry_1 = tk.Entry(self)
        entry_1.pack(side="top")

        label_2 = tk.Label(self, text="Password")
        label_2.pack(side="top")

        entry_2 = tk.Entry(self)
        entry_2.pack(side="top")


        button_1 = tk.Button(self, text="Login", default='active',
                            command=lambda: controller.show_frame("HomePage"))
        button_1.pack()

        button_2 = tk.Button(self, text="Register",
                            command=lambda: controller.show_frame("RegistrationPage"))
        button_2.pack()

# This is the HomePage Class that will show the home page screen once the user has logged in.
class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="This is home page once logged in!", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Logout",
                           command=lambda: controller.show_frame("LoginPage"))
        button.pack()

# This is the RegistrationPage Class that will show the registration page once the user attempts to register.
class RegistrationPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Registration", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        label_1 = tk.Label(self, text="Full Name")
        label_1.pack(side="top")

        entry_1 = tk.Entry(self)
        entry_1.pack(side="top")

        label_2 = tk.Label(self, text="Email")
        label_2.pack(side="top")

        entry_2 = tk.Entry(self)
        entry_2.pack(side="top")

        label_3 = tk.Label(self, text="Desired Username")
        label_3.pack(side="top")

        entry_3 = tk.Entry(self)
        entry_3.pack(side="top")

        label_4 = tk.Label(self, text="Desired Password")
        label_4.pack(side="top")

        entry_4 = tk.Entry(self)
        entry_4.pack(side="top")

        button = tk.Button(self, text="Submit",
                           command=lambda: controller.show_frame("LoginPage"))
        button.pack()

# This is the loop to keep application running.
if __name__ == "__main__":
    app = BeweeveApp()
    app.mainloop()