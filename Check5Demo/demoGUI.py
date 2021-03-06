# Created by Thomas Schmidt 3/5/2017
# This simple program creates the basic GUI for the BeweeveApp

#TEST

import Tkinter as tk   

from Database import *

DATABASE = Database() #added by Alex Lambert 3/9/17

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

        self.title("BeWeeve")
        self.frames = {}
        
        for F in (LoginPage, HomePage, RegistrationPage, RegisterContestPage, EventSchedulePage, JudgesListPage):
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

        label = tk.Label(self, text="BeWeeve", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        label_1 = tk.Label(self, text="User ID")
        label_1.pack(side="top")

        self.entry_1 = tk.Entry(self)
        self.entry_1.pack(side="top")

        button = tk.Button(self, text='Login', command=lambda: self.reg_Click())
        button.pack()

        button_2 = tk.Button(self, text="Register",
                            command=lambda: controller.show_frame("RegistrationPage"))
        button_2.pack()

    def reg_Click(self):
        """check login credentials"""
        #Need non string exception

        #User input
        #Overrides default input
        global userID
        userID = self.entry_1.get()

        if DATABASE.doesUserExist(userID):
            self.controller.show_frame('HomePage')
        else:
            label = tk.Label(self, text='FAILURE!')
            label.pack()

# This is the HomePage Class that will show the home page screen once the user has logged in.
class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="This is home page once logged in!", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        
        button2 = tk.Button(self, text = "Event Schedule", command=lambda: controller.show_frame("EventSchedulePage")) 
        button3 = tk.Button(self, text = "Register for Contest", command=lambda: controller.show_frame("RegisterContestPage"))
        button4 = tk.Button(self, text = "Judges", command=lambda:controller.show_frame("JudgesListPage"))

        button3.pack()
        button4.pack()
        button2.pack()
    

        button = tk.Button(self, text="Logout",
                           command=lambda: controller.show_frame("LoginPage"))
        button.pack()

""" Author: Phansa Chaonpoj\n
            UW NetID: phansac\n
            Date: 3/12/17\n
           lists out all the judges frame.\n"""
class JudgesListPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.label = tk.Label(self, text = "list of judges")
        self.pack(side="top", fill= "x", pady=10)

        
        button = tk.Button(self, text= "Back", command=lambda:controller.show_frame("HomePage"))
        button.pack()

        #sample added judges to show things
        #TODO, when it is printed out, its fucked up
        DATABASE.addJudge(['Toad', 'cranet@uw.edu', [str(3), str(4)]])
        DATABASE.addJudge(['Alex', 'alamb25@uw.edu', ['NONE', 'ONE, TWO']])
        DATABASE.addJudge(['Caleb', 'caleb447@uw.edu', ['NONE', 'TWO', 'FOUR']])

        judgeslist = DATABASE.getAllJudges()
        judges = []
        for judge in judgeslist:
            judges.append(judge)
            print judge

        printjudge = []
        judgeslist = DATABASE.getAllJudges()
        for row in judgeslist:
            temp = row[0], row[1], row[2], ' '.join(row[3])
            label = tk.Message(self, text= temp, width = 400)
       
        #when printed here, everything is a mess but it grabs the judges from database
        #label = tk.Message(self, text= judges, width = 200)
        label.pack()

""" Author: Phansa Chaonpoj\n
            UW NetID: phansac\n
            Date: 3/12/17\n
           this is the event schedule page.\n"""
class EventSchedulePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller 

        self.label = tk.Label(self, text= "Event Schedule")
        self.pack(side="top", fill ="x", pady=10)

        button = tk.Button(self, text= "Back", command=lambda:controller.show_frame("HomePage"))
        button.pack()
        #show listings for time and schedule.
        DATABASE.intializeTables()
        #somehow show all the lists of time and categries ?


""" Author: Phansa Chaonpoj\n
            Evan Penru\n
            Date: 3/12/17\n
           register for contest, saves the selected menu
           and sends to the data base for that user.\n"""
class RegisterContestPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.label = tk.Label(self, text="Register for Contest")
        self.pack(side="top", fill="x", pady=10)

        DATABASE.addCategory(['get lit', ';)', '4:20'])
        DATABASE.addCategory(['eat', ';)', '4:20'])
        DATABASE.addCategory(['sleep', ';)', '4:20'])


        tkvar = tk.StringVar(master=None)
        tkvar.set("Options")

        #TODO: get rid of brackets
        #populate dropdown menu with each category's name
        choiceIds = DATABASE.getAllCategoriesIDs()
        choices = []
        for id in choiceIds:
            choices.append(DATABASE.getCategory(id)[1])

        #DEBUGchoices = ['a', 'b', 'c']


        popupMenu = tk.OptionMenu(self, tkvar, *choices)
        popupMenu.pack()
        

        
        #after they click register then they will go back to the home page
        button = tk.Button(self, text = "register", command=lambda: registerForCategory(self))
        button.pack()

        cancelButton = tk.Button(self, text = "Cancel", command=lambda: controller.show_frame("HomePage"))
        cancelButton.pack()


        #registers the user for the selected category
        def registerForCategory(self):
            #update Database
            temp = DATABASE.getCategory(userID)
            temp.append("")#currently selected category
            
            #get selected category from the dropmenu
            selectedCate = tkvar.get()
            print selectedCate

            DATABASE.modifyContestant(userID, selectedCate) 

            #return to homepage
            controller.show_frame("HomePage")

            #test if it sent to database 
            #print "user ID %s \n" %userID
            #print "user selected category %s \n" %selectedCate
            #tempUser = DATABASE.getContestant(userID)
            #print tempUser 

            
        

# This is the RegistrationPage Class that will show the registration page once the user attempts to register.
class RegistrationPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.label = tk.Label(self, text="Registration", font=TITLE_FONT)
        self.label.pack(side="top", fill="x", pady=10)

        self.label_1 = tk.Label(self, text="Full Name")
        self.nameText = tk.StringVar()
        self.label_1.pack(side="top")
        tk.Entry(self, textvariable=self.nameText).pack()

        self.label_2 = tk.Label(self, text="Email")
        self.emailText = tk.StringVar()
        self.label_2.pack(side="top")
        tk.Entry(self, textvariable=self.emailText).pack()

        button = tk.Button(self, text="Submit",
                           command=self.regClick)
        button.pack()

        backButton = tk.Button(self, text='Back', 
                               command=lambda: controller.show_frame("HomePage"))
        backButton.pack()

    def regClick(self):
        """Gets the user input"""
        #Need non string exception

        #User input
        #Overrides default input
        name = self.nameText.get()
        email = self.emailText.get()

        userID = self.sendToDatabase(name, email)    #added by Alex Lambert 3/9/17
        DATABASE.commit()                            #added by Alex Lambert 3/9/17
        self.displayUserID(userID)
        #Test input
        # print name
        # print email

    def sendToDatabase(self, name, email):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/9/17\n
            Add contestant to the Database"""

        entry = [name, email, '']
        return  DATABASE.addContestant(entry)

    def displayUserID(self, userID):
        userID = tk.Label(self, text=userID)
        userID.pack()
# This is the loop to keep application running.
if __name__ == "__main__":
    app = BeweeveApp()
    app.mainloop()