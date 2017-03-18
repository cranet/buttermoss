""" Author: Alex Lambert\n
    UW NetID: alamb25\n
    Date: 3/11/17\n
    The main for the BeweeveApp"""
from BeWeave import *
from Database import Database
from User import User

DATABASE = Database()
CURRENT_USER = User()

#This is the loop to keep application running
if __name__ == "__main__":
    if not DATABASE.doesUserExist(12345):
        DATABASE.addAdmin([12345, 'Jeff Weiss', 'jawit@uw.edu'])
        DATABASE.commit()
    app = BeWeeveApp()
    app.mainloop()
