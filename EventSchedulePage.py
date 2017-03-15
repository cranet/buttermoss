import Tkinter as tk   
import ttk

from BeweeveMain import DATABASE

TITLE_FONT = ("Helvetica", 20, "bold")

class EventSchedulePage(tk.Frame):
    """ Author: Evan Pernu\n
    UW NetID: epernu\n
    Date: 3/11/2017\n
    This page displays an event calendar"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        backButton = tk.Button(self, text='Back', 
                               command=lambda: controller.show_frame("HomePage"))                      
        backButton.grid(row=6, column=1)

        #initialize scrollable list
        eventNameList = tk.Listbox(self, width=20, height=20, font=("Helvetica", 12))
        eventNameList.grid(row=2, column=1, rowspan=5)
        scrollbar = tk.Scrollbar(self, orient="vertical")
        scrollbar.config(command=eventNameList.yview)
        scrollbar.grid(row=2, column=5, rowspan=5)  #TODO: scrollbar may not work correctly
        eventNameList.config(yscrollcommand=scrollbar.set)
        eventNameList.bind("<Button-1>", self.selectItem)

        #DATABASE.addCategory(['Toad Contesy', 'fun', '9:30am'])
        #DATABASE.addCategory(['Alex Contest', 'more fun', '10:30am'])
        #DATABASE.addCategory(['Caleb Contest', 'less fun', '11:45am'])

        #add all categories to list
        temp = DATABASE.getAllCategoriesIDs()
        for id in temp:
            eventNameList.insert(tk.END, DATABASE.getCategory(id)[1])

        #initialize selection display
        label1 = tk.Label(self, text="ID:", font=("Helvetica", 10))
        label2 = tk.Label(self, text="Name:", font=("Helvetica", 10))
        label3 = tk.Label(self, text="Description:", font=("Helvetica", 10))
        label4 = tk.Label(self, text="Time:", font=("Helvetica", 10))

        label1.grid(row=2, column=3)
        label2.grid(row=3, column=3)
        label3.grid(row=4, column=3)
        label4.grid(row=5, column=3)

        

    def selectItem(self, event):
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        index = int(widget.curselection()[0])

        temp = DATABASE.getAllCategoriesIDs()

        info1 = tk.Label(self, text=DATABASE.getCategory(temp[index])[0], font=("Helvetica", 10))
        info2 = tk.Label(self, text=DATABASE.getCategory(temp[index])[1], font=("Helvetica", 10))
        info3 = tk.Label(self, text=DATABASE.getCategory(temp[index])[2], font=("Helvetica", 10))
        info4 = tk.Label(self, text=DATABASE.getCategory(temp[index])[3], font=("Helvetica", 10))

        info1.grid(row=2, column=4)
        info2.grid(row=3, column=4)
        info3.grid(row=4, column=4)
        info4.grid(row=5, column=4)

        #self.info1.config(text=DATABASE.getCategory(temp[value])[0]) 
        #info2.config(text=) 
        #info3.config(text=) 
        #info4.config(text=)    

