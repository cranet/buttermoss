import Tkinter as tk   

from BeweeveMain import DATABASE, CURRENT_USER

TITLE_FONT = ("Helvetica", 20, "bold")

selectedUser = 0
class AdminContestantsPage(tk.Frame):
    """ Author: Evan Pernu\n
    UW NetID: epernu\n
    Date: 3/11/2017\n
    This is the page that allows admins to view and edit contestants"""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        selectedUser = 0
        #ADDING CONTESTANTS FOR TESTING
        DATABASE.addContestant(['Toad', 'cranet@uw.edu', ['NONE']])
        DATABASE.addContestant(['Alex', 'alamb25@uw.edu', ['NONE' 'ONE ONE', 'TWO']])
        DATABASE.addContestant(['Caleb', 'caleb447@uw.edu', ['NONE', 'TWO', 'FOUR']])
        #initialize buttons
        backButton = tk.Button(self, text='Back', 
                               command=lambda: controller.show_frame("AdminPage"))                       
        saveButton = tk.Button(self, text='Save Changes', command=lambda: self.saveChanges())
        addButton = tk.Button(self, text='New Contestant', command=lambda: self.addItem())
        deleteButton = tk.Button(self, text='Delete Selected', command=lambda: self.delete())       

        backButton.grid(row=7, column=2)  
        addButton.grid(row=7, column=3)
        deleteButton.grid(row=7, column=4)        
        saveButton.grid(row=7, column=5)
        
        #initialize scrollable list
        self.nameList = tk.Listbox(self, width=20, height=20, font=("Helvetica", 12))
        self.nameList.grid(row=2, column=1, rowspan=5)
        scrollbar = tk.Scrollbar(self, orient="vertical")
        scrollbar.config(command=self.nameList.yview)
        scrollbar.grid(row=2, column=5, rowspan=5)  #TODO: scrollbar may not work correctly
        self.nameList.config(yscrollcommand=scrollbar.set)
        self.nameList.bind("<Button-1>", self.selectItem)

        #add all categories to list
        self.refresh()

        #initialize selection display
        label1 = tk.Label(self, text="ID:", font=("Helvetica", 10))
        label2 = tk.Label(self, text="Name:", font=("Helvetica", 10))
        label3 = tk.Label(self, text="Email:", font=("Helvetica", 10))
        label4 = tk.Label(self, text="Categories:", font=("Helvetica", 10))

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
        temp = DATABASE.getAllContestantUserIDs()

        #clear all entry boxes
        self.entry2.delete(0, tk.END)
        self.entry3.delete(0, tk.END)
        self.entry4.delete(0, tk.END)

        #set all entry boxes to selection's values
        global selectedUser 
        selectedUser = DATABASE.getContestant(temp[index])
        self.info1.config(text=DATABASE.getContestant(temp[index])[0])
        self.entry2.insert(0,DATABASE.getContestant(temp[index])[1])
        self.entry3.insert(0,DATABASE.getContestant(temp[index])[2])
        self.entry4.insert(0,DATABASE.getContestant(temp[index])[3])

    #TODO: currently cannot modify email
    #writes the values of the entry boxes to the selection in database
    def saveChanges(self):
         #add the entries to database. and to list.
         #Grabbing ID from selected User, and grabbing information to be updated from box.BaseException
         # if the user already exists, we modify. else it's a new contestant. 
         #print "printing selected user before changing"
         #print selectedUser
         if (self.selectedUser == 0):
                #adding new contestant. 
            entry = [self.entry2.get(), self.entry3.get(), self.entry4.get()]
            print entry
            DATABASE.addContestant(entry)
            DATABASE.commit()

         elif DATABASE.doesUserExist(selectedUser[0]):
            DATABASE.modifyContestant(selectedUser[0], self.entry4.get()) 
            DATABASE.commit()    

         self.update()
         self.refresh()
    
    #TODO: list doesnt totally refresh until you go back
    #refreshes the list
    def refresh(self):
        #clear list
        self.nameList.delete(0, tk.END) 
        temp = DATABASE.getAllContestantUserIDs()
        for id in temp:
            self.nameList.insert(tk.END, DATABASE.getContestant(id)[1])
        self.update() #changes the look of the list.

    #connects to new contestant so it should clear the current info.
    def addItem(self):
        #DATABASE.sendToDatabase("New User", "")
       # DATABASE.commit()  

        self.selectedUser = 0
        #print "clearing selected user"
        #print selectedUser
        self.info1.config(text="")
        self.entry2.delete(0, tk.END)
        self.entry3.delete(0, tk.END)
        self.entry4.delete(0, tk.END)


    #TODO
    #deletes the selection from list and database.
    def delete(self):
        #parsing through the index
        #temp = DATABASE.getAllContestantUserIDs()
        selected = map(int, self.nameList.curselection())
        
        pos = 0
        for i in selected:
            idx = int(i) - pos
            self.nameList.delete(idx, idx)
            pos = pos + 1
        #clear the forms.
        self.entry2.delete(0, tk.END)
        self.entry3.delete(0, tk.END)
        self.entry4.delete(0, tk.END)

      
        #delete from database.
        DATABASE.removeContestant(selectedUser[0]) 
        DATABASE.commit()

