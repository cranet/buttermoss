""" Author: Alex Lambert\n
        UW NetID: alamb25\n
        Date: 3/11/17\n
        The main for the BeweeveApp"""

from BeweeveApp import *
from Database import Database
from User import User

DATABASE = Database() 
CURRENT_USER = User()


# This is the loop to keep application running.
if __name__ == "__main__":
    if not DATABASE.doesUserExist(12345):
        DATABASE.addAdmin([12345, 'Jeff Weiss', 'jawit@uw.edu'])
        
        # DATABASE.addContestant(['Alex Lambert', 'alamb25@uw.edu', ''])
        # DATABASE.addCategory(['Toad Contesy', 'fun', '9:30am'])
        DATABASE.addCategory(['Alex Contest', 'more fun', '10:30am'])
        # DATABASE.addCategory(['Caleb Contest', 'less fun', '11:45am'])
        # DATABASE.addJudge(['Judge Toad', 'cranet@uw.edu', [str(3), str(4)]])
        # DATABASE.addJudge(['Judge Alex', 'alamb25@uw.edu', ['NONE', 'ONE, TWO']])
        # DATABASE.addJudge(['Judge Caleb', 'caleb447@uw.edu', ['NONE', 'TWO', 'FOUR']])
        DATABASE.commit()
    app = BeweeveApp()
    app.mainloop()