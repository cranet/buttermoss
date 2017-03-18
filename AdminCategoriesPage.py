"""Admin Categories Page"""
import Tkinter as tk
from BeweeveMain import DATABASE #CURRENT_USER

TITLE_FONT = ("Helvetica", 20, "bold")

class AdminCategoriesPage(tk.Frame):
    """ Author: Evan Pernu\n
    UW NetID: epernu\n
    Date: 3/11/2017\n
    This is the page that allows admins to view and edit categories"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.selectedCategory = 0

        #Initialize buttons
        self.backButton = tk.Button(self, text='Back',
                                    command=lambda: controller.show_frame("AdminPage"))
        self.saveButton = tk.Button(self, text='Save Changes', command=lambda: self.saveChanges())
        self.addButton = tk.Button(self, text='New Event', command=lambda: self.addItem())
        self.deleteButton = tk.Button(self, text='Delete Selected',
                                      command=lambda: self.deleteSelected())

        self.backButton.grid(row=7, column=2)
        self.addButton.grid(row=7, column=3)
        self.deleteButton.grid(row=7, column=4)
        self.saveButton.grid(row=7, column=5)

        #Initialize scrollable list
        self.eventNameList = tk.Listbox(self, width=20, height=20, font=("Helvetica", 12))
        self.eventNameList.grid(row=2, column=1, rowspan=5)
        self.scrollbar = tk.Scrollbar(self, orient="vertical")
        self.scrollbar.config(command=self.eventNameList.yview)
        self.scrollbar.grid(row=2, column=5, rowspan=5)
        self.eventNameList.config(yscrollcommand=self.scrollbar.set)
        self.eventNameList.bind("<Button-1>", self.selectItem)

        #Add all categories to list
        self.refresh()

        #Initialize selection display
        self.label1 = tk.Label(self, text="ID:", font=("Helvetica", 10))
        self.label2 = tk.Label(self, text="Name:", font=("Helvetica", 10))
        self.label3 = tk.Label(self, text="Description:", font=("Helvetica", 10))
        self.label4 = tk.Label(self, text="Time:", font=("Helvetica", 10))

        self.label1.grid(row=2, column=3)
        self.label2.grid(row=3, column=3)
        self.label3.grid(row=4, column=3)
        self.label4.grid(row=5, column=3)

        self.info1 = tk.Label(self, text="", font=("Helvetica", 10))
        self.entry2 = tk.Entry(self)
        self.entry3 = tk.Entry(self)
        self.entry4 = tk.Entry(self)

        self.info1.grid(row=2, column=4)
        self.entry2.grid(row=3, column=4)
        self.entry3.grid(row=4, column=4)
        self.entry4.grid(row=5, column=4)

    #Display selection's information
    def selectItem(self, event):
        """ Author: Evan Pernu\n
            UW NetID: epernu\n
            Date: 3/11/2017\n"""
        widget = event.widget
        index = int(widget.curselection()[0])
        temp = DATABASE.getAllCategoriesIDs()

        #Clear all entry boxes
        self.entry2.delete(0, tk.END)
        self.entry3.delete(0, tk.END)
        self.entry4.delete(0, tk.END)

        #Getting selected category
        self.selectedCategory = DATABASE.getCategory(temp[index])
        print self.selectedCategory

        #Set all entry boxes to selection's values
        self.info1.config(text=DATABASE.getCategory(temp[index])[0])
        self.entry2.insert(0, DATABASE.getCategory(temp[index])[1])
        self.entry3.insert(0, DATABASE.getCategory(temp[index])[2])
        self.entry4.insert(0, DATABASE.getCategory(temp[index])[3])

    #Writes the values of the entry boxes to the selection in database
    #If the selectedcategory is zero add new else modify category.
    def saveChanges(self):
        """ Author: Evan Pernu\n
            UW NetID: epernu\n
            Date: 3/11/2017\n"""
        if self.selectedCategory == 0:
            #Adding new category
            entry = [self.entry2.get(), self.entry3.get(), self.entry4.get()]
            DATABASE.addCategory(entry)
        else:
            entry = [self.entry2.get(), self.entry3.get(), self.entry4.get()]
            DATABASE.modifyCategory(self.selectedCategory[0], entry)

        DATABASE.commit()
        self.refresh()

    #Refreshes the list
    def refresh(self):
        """ Author: Evan Pernu\n
            UW NetID: epernu\n
            Date: 3/11/2017\n"""
        #Clear list
        self.eventNameList.delete(0, tk.END)
        temp = DATABASE.getAllCategoriesIDs()
        for usrID in temp:
            self.eventNameList.insert(tk.END, DATABASE.getCategory(usrID)[1])

    #Adds a new, empty item
    def addItem(self):
        """ Author: Evan Pernu\n
            UW NetID: epernu\n
            Date: 3/11/2017\n"""
        self.selectedCategory = 0
        self.info1.config(text="")
        self.entry2.delete(0, tk.END)
        self.entry3.delete(0, tk.END)
        self.entry4.delete(0, tk.END)


    #Deletes the selected category added by Phansa.
    def deleteSelected(self):
        """ Author: Evan Pernu\n
            UW NetID: epernu\n
            Date: 3/11/2017\n"""
        #Parsing through the index
        selected = map(int, self.eventNameList.curselection())

        pos = 0
        for i in selected:
            idx = int(i) - pos
            self.eventNameList.delete(idx, idx)
            pos = pos + 1

        #Clear the forms.
        self.entry2.delete(0, tk.END)
        self.entry3.delete(0, tk.END)
        self.entry4.delete(0, tk.END)

        #Delete from database.
        DATABASE.removeCategory(self.selectedCategory[0])
        self.refresh()
