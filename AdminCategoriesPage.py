import Tkinter as tk   

from BeweeveMain import DATABASE, CURRENT_USER

TITLE_FONT = ("Helvetica", 20, "bold")

class AdminCategoriesPage(tk.Frame):
    """ Author: Evan Pernu\n
    UW NetID: epernu\n
    Date: 3/11/2017\n
    This is the page that allows admins to view and edit categories"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #initialize buttons
        backButton = tk.Button(self, text='Back', 
                               command=lambda: controller.show_frame("AdminPage"))                       
        saveButton = tk.Button(self, text='Save Changes', command=lambda: self.saveChanges())
        addButton = tk.Button(self, text='New Event', command=lambda: self.addItem())
        deleteButton = tk.Button(self, text='Delete Selected', command=lambda: self.delete())       

        backButton.grid(row=7, column=2)  
        addButton.grid(row=7, column=3)
        deleteButton.grid(row=7, column=4)        
        saveButton.grid(row=7, column=5)
        
        #initialize scrollable list
        self.eventNameList = tk.Listbox(self, width=20, height=20, font=("Helvetica", 12))
        self.eventNameList.grid(row=2, column=1, rowspan=5)
        scrollbar = tk.Scrollbar(self, orient="vertical")
        scrollbar.config(command=self.eventNameList.yview)
        scrollbar.grid(row=2, column=5, rowspan=5)  #TODO: scrollbar may not work correctly
        self.eventNameList.config(yscrollcommand=scrollbar.set)
        self.eventNameList.bind("<Button-1>", self.selectItem)

        #add test events
        DATABASE.addCategory(['Toad Contesy', 'fun', '9:30am'])
        DATABASE.addCategory(['Alex Contest', 'more fun', '10:30am'])
        DATABASE.addCategory(['Caleb Contest', 'less fun', '11:45am'])

        #add all categories to list
        self.refresh()

        #initialize selection display
        label1 = tk.Label(self, text="ID:", font=("Helvetica", 10))
        label2 = tk.Label(self, text="Name:", font=("Helvetica", 10))
        label3 = tk.Label(self, text="Description:", font=("Helvetica", 10))
        label4 = tk.Label(self, text="Time:", font=("Helvetica", 10))

        label1.grid(row=2, column=3)
        label2.grid(row=3, column=3)
        label3.grid(row=4, column=3)
        label4.grid(row=5, column=3)

        self.info1 = tk.Label(self, text="", font=("Helvetica", 10))
        self.entry2 = tk.Entry(self)
        self.entry3 = tk.Entry(self)
        self.entry4 = tk.Entry(self)

        self.info1.grid(row=2, column=4)
        self.entry2.grid(row=3, column=4)
        self.entry3.grid(row=4, column=4)
        self.entry4.grid(row=5, column=4)

        
    #display selection's information
    def selectItem(self, event):
        widget = event.widget
        selection=widget.curselection()
        index = int(widget.curselection()[0])
        temp = DATABASE.getAllCategoriesIDs()

        #clear all entry boxes
        self.entry2.delete(0, tk.END)
        self.entry3.delete(0, tk.END)
        self.entry4.delete(0, tk.END)

        #set all entry boxes to selection's values
        self.info1.config(text=DATABASE.getCategory(temp[index])[0])
        self.entry2.insert(0,DATABASE.getCategory(temp[index])[1])
        self.entry3.insert(0,DATABASE.getCategory(temp[index])[2])
        self.entry4.insert(0,DATABASE.getCategory(temp[index])[3])

    #writes the values of the entry boxes to the selection in database
    def saveChanges(self):
        DATABASE.modifyCategory(int(self.info1.cget('text')), [self.entry2.get(), self.entry3.get(), self.entry4.get()])
        DATABASE.commit()
        self.refresh()
    
    #TODO: list doesnt totally refresh until you go back
    #refreshes the list
    def refresh(self):
        #clear list
        self.eventNameList.delete(0, tk.END)

        temp = DATABASE.getAllCategoriesIDs()
        for id in temp:
            self.eventNameList.insert(tk.END, DATABASE.getCategory(id)[1])

    #adds a new, empty item
    def addItem(self):
        DATABASE.addCategory(['New Event', '', ''])
        DATABASE.commit()
        self.refresh()

    #TODO
    #deletes the selection
    def delete(self):
        self.refresh()



        
