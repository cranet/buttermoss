import Tkinter as tk   
import ttk

from BeweeveMain import DATABASE, CURRENT_USER

TITLE_FONT = ("Helvetica", 20, "bold")

class EventSchedulePage(tk.Frame):
    """ Author: Evan Pernu\n
    UW NetID: epernu\n
    Date: 3/14/2017\n
    This page displays an event calendar"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.backButton = tk.Button(self, text='Back',
                                    command=lambda: controller.show_frame("HomePage"))
        self.regButton = tk.Button(self, text='Register for Selected',
                                   command=lambda: self.registerForCategory())

        self.backButton.grid(row=7, column=1)
        self.regButton.grid(row=7, column=3)

        #initialize scrollable list
        self.eventNameList = tk.Listbox(self, width=20, height=20, font=("Helvetica", 12))
        self.eventNameList.grid(row=2, column=1, rowspan=5)
        self.scrollbar = tk.Scrollbar(self, orient="vertical")
        self.scrollbar.config(command=self.eventNameList.yview)
        self.scrollbar.grid(row=2, column=5, rowspan=5)
        self.eventNameList.config(yscrollcommand=self.scrollbar.set)
        self.eventNameList.bind("<Button-1>", self.selectItem)

        #add all categories to list
        temp = DATABASE.getAllCategoriesIDs()
        for usrID in temp:
            self.eventNameList.insert(tk.END, DATABASE.getCategory(usrID)[1])

        #initialize selection display
        self.label1 = tk.Label(self, text="ID:", font=("Helvetica", 10))
        self.label2 = tk.Label(self, text="Name:", font=("Helvetica", 10))
        self.label3 = tk.Label(self, text="Description:", font=("Helvetica", 10))
        self.label4 = tk.Label(self, text="Time:", font=("Helvetica", 10))

        self.label1.grid(row=2, column=3)
        self.label2.grid(row=3, column=3)
        self.label3.grid(row=4, column=3)
        self.label4.grid(row=5, column=3)

        self.info1 = tk.Label(self, text="", font=("Helvetica", 10))
        self.info2 = tk.Label(self, text="", font=("Helvetica", 10))
        self.info3 = tk.Label(self, text="", font=("Helvetica", 10))
        self.info4 = tk.Label(self, text="", font=("Helvetica", 10))

        self.info1.grid(row=2, column=4)
        self.info2.grid(row=3, column=4)
        self.info3.grid(row=4, column=4)
        self.info4.grid(row=5, column=4)

        
    #display selection's information
    def selectItem(self, event):
        widget = event.widget
        selection = widget.curselection()
        index = int(widget.curselection()[0])
        temp = DATABASE.getAllCategoriesIDs()

        #set all labels to selection's values
        self.info1.config(text=DATABASE.getCategory(temp[index])[0])
        self.info2.config(text=DATABASE.getCategory(temp[index])[1])
        self.info3.config(text=DATABASE.getCategory(temp[index])[2])
        self.info4.config(text=DATABASE.getCategory(temp[index])[3])

        self.selectedCategory = DATABASE.getCategory(temp[index])[1]

    #registers the user for the selected category
    def registerForCategory(self):
        DATABASE.modifyContestant(CURRENT_USER.userID, self.selectedCategory)
        DATABASE.commit()
        #return to homepage
        self.controller.show_frame("HomePage")

