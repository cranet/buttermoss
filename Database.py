import sqlite3
import os

class Database(object):
    """ Author: Alex Lambert\n
        UW NetID: alamb25\n
        Date: 3/7/17\n
        Database object that holds information about events"""

    def __init__(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Constructor"""
        self.conn = sqlite3.connect('example.db')
        self.cursor = self.conn.cursor()
        if not os.path.isfile('example.db'):
            self.intializeTables()

    def intializeTables(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Initializes tables insuserIDe the Databse"""

        self.cursor.execute('''CREATE TABLE CONTESTANTS
                            (userID INT PRIMARY KEY     NOT NULL,
                            NAME            TEXT    NOT NULL,
                            EMAIL           TEXT    NOT NULL,
                            CATEGORIES      TEXT    NOT NULL);''')
        self.cursor.execute('''CREATE TABLE JUDGES
                            (userID INT PRIMARY KEY     NOT NULL,
                            NAME            TEXT    NOT NULL,
                            EMAIL           TEXT    NOT NULL,
                            CATEGORIES      TEXT    NOT NULL);''')
        self.cursor.execute('''CREATE TABLE ADMINS
                            (userID INT PRIMARY KEY     NOT NULL,
                            NAME            TEXT    NOT NULL,
                            EMAIL           TEXT    NOT NULL);''')
        self.cursor.execute('''CREATE TABLE CATEGORIES
                            (userID INT PRIMARY KEY     NOT NULL,
                            NAME            TEXT    NOT NULL,
                            ABOUT           TEXT    NOT NULL,
                            START_TIME      TEXT    NOT NULL);''')

    def commit(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Commits changes to the Database\n
            To be used with the GUI"""
        self.conn.commit()

    def addContestant(self, useruserID, name, email, categories):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Add contestant to the Database"""
        entry = [useruserID, name, email, categories]
        self.cursor.execute("INSERT INTO CONTESTANTS (userID,NAME,EMAIL,CATEGORIES) \
                            VALUES (?, ?, ?, ?)", entry)

    def getContestant(self, useruserID):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Gets contestant from the Database using unique userID"""
        toReturn = self.cursor.execute('SELECT * FROM CONTESTANTS WHERE userID=?', (useruserID,))
        return toReturn

    def getAllContestant(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Returns all contestants from the Database"""
        toReturn = self.cursor.execute('SELECT * FROM CONTESTANTS')
        return toReturn

    def getAllContestantuserID(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Returns all contestants' unique userIDs from the Database"""
        return set(self.cursor.execute('SELECT userID FROM contestants').fetchall())

    def modifyContestant(self, userID, t):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Modifies existing Contestant using the unique userID\n
            Changes the contestant's categories list"""
        catList = " ".join(t)
        te = [catList, userID]
        self.cursor.execute('UPDATE set categories=? where userID=?', te)

    def removeContestant(self, userID):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Removes the contestant corresponding to the unique userIDs from the Database\n
            Used for when a contestant gets moved to being a Judge"""
        self.conn.execute("DELETE FROM contestants WHERE userID=?", (userID,))

    def addJudge(self, userID, name, email, categories):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Adds the judge to the database"""
        thing = [userID, name, email, categories]
        self.cursor.execute("INSERT INTO contestants VALUES (?, ?, ?, ?)", thing)

    def getJudge(self, userID):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Returns the judge from the Database using the unique id"""
        self.cursor.execute('SELECT userID, name, email, categories FROM contestants WHERE userID=?', (userID,))
        return self.cursor.fetchone()

    def removeJudge(self, userID):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Returns all contestants from the Database"""
        self.conn.execute("DELETE FROM contestants WHERE userID=?", (userID,))

    def closeDB(self):
        """ Author: Alex Lambert\n
            UWnetID: alamb25\n
            Date: 3/7/17\n
            Closes the database\n
            DOES NOT COMMIT CHANGES!"""
        self.conn.close()
