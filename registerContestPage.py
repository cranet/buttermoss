import Tkinter as tk   

from BeweeveMain import DATABASE

TITLE_FONT = ("Helvetica", 20, "bold")

class registerContestPage(tk.Frame):
    """Author: Phansa Chaonpoj\n
    Date: 3/9/2017\n
    UW NetID: phansac\n
    Author: Evan Pernu\n
    UW NetID: epernu\n
    Date: 3/11/2017\n
    This is page used to register a contestand for an event."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.label = tk.Label(self, text="Register for Contest")
        self.pack(side="top", fill="x", pady=10)

        tkvar = tk.StringVar(master=None)
        tkvar.set("Select a Category")

        #TODO: get rid of brackets
        #populate dropdown menu with each category's name
        choiceIds = DATABASE.getAllCategoriesIDs()
        choices = []
        for id in choiceIds:
            choices.append(DATABASE.getCategory(id)[1])


        #popupMenu = tk.OptionMenu(self, tkvar, *choices)
        #popupMenu.pack()
        
        button = tk.Button(self, text = "register", command=lambda: self.registerForCategory())
        button.pack()

        backButton = tk.Button(self, text='Back', 
                               command=lambda: controller.show_frame("HomePage"))
                               
        backButton.pack()



    #registers the user for the selected category
    def registerForCategory(self):
        #TODO: register the user for the selected category

        #return to homepage
        self.controller.show_frame("HomePage")