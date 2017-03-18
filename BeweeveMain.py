""" Author: Alex Lambert\n
    UW NetID: alamb25\n
    Date: 3/11/17\n
    The main for the BeweeveApp"""
from BeweeveApp import BeweeveApp
from Database import Database
from User import User

DATABASE = Database()
CURRENT_USER = User()

#This is the loop to keep application running
if __name__ == "__main__":
    if not DATABASE.doesUserExist(12345):
        DATABASE.addAdmin([12345, 'Jeff Weiss', 'jawit@uw.edu'])
        DATABASE.addCategory(['Alex Contest', 'more fun', '10:30am'])
        DATABASE.commit()
    app = BeweeveApp()
    app.mainloop()
