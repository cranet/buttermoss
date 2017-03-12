""" Author: Alex Lambert\n
        UW NetID: alamb25\n
        Date: 3/11/17\n
        The main for the BeweeveApp"""
from BeweeveApp import *
from Database import Database

DATABASE = Database() #added by Alex Lambert 3/11/17

# This is the loop to keep application running.
if __name__ == "__main__":
    app = BeweeveApp()
    app.mainloop()