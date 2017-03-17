import Tkinter as tk   

from BeweeveMain import DATABASE, CURRENT_USER

TITLE_FONT = ("Helvetica", 20, "bold")

class registerContestPage(tk.Frame):
    """Author: Phansa Chaonpoj\n
    Date: 3/9/2017\n
    UW NetID: phansac\n
    Author: Evan Pernu\n
    UW NetID: epernu\n
    Date: 3/11/2017\n
    This is page used to register a contestand for an event."""

    def __init__(self, parent, controller): #need user id to register to data base.
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.label = tk.Label(self, text="Register for Contest")
        self.pack(side="top", fill="x", pady=10)

        tkvar = tk.StringVar(self)
        tkvar.set("Select a Category")

        #populate dropdown menu with each category's name
        categories = DATABASE.getAllCategories();
        #getting categories and adding each into choices.
        categoryNames = {}
        for x in categories:
            #choices.append(DATABASE.getCategory(id)[1])
            categoryNames[x[1]] = x[0]

        popupMenu = tk.OptionMenu(self, tkvar, *categoryNames.keys())
        popupMenu.pack()

        button = tk.Button(self, text="register", command=lambda: 
                           self.registerForCategory(categoryNames.get(tkvar.get())))
        button.pack()

        backButton = tk.Button(self, text='Back', 
                               command=lambda: controller.show_frame("HomePage"))                    
        backButton.pack()

    #registers the user for the selected category
    def registerForCategory(self, category):
        DATABASE.modifyContestant(CURRENT_USER.userID, category)
        #return to homepage
        self.controller.show_frame("HomePage")