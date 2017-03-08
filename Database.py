import sqlite3
import random

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
        self.intializeTables()
        self.usedIDs = set(self.getAllContestantUserIDs() +
                           self.getAllJudgesUserIDs() +
                           self.getAllAdminsUserIDs())

        

    def intializeTables(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Initializes tables insuserIDe the Database"""

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS CONTESTANTS
                            (USERID INT PRIMARY KEY     NOT NULL,
                            NAME                TEXT    NOT NULL,
                            EMAIL               TEXT    NOT NULL,
                            CATEGORIES          TEXT    NOT NULL);''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS JUDGES
                            (USERID INT PRIMARY KEY     NOT NULL,
                            NAME                TEXT    NOT NULL,
                            EMAIL               TEXT    NOT NULL,
                            CATEGORIES          TEXT    NOT NULL);''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS ADMINS
                            (USERID INT PRIMARY KEY     NOT NULL,
                            NAME                TEXT    NOT NULL,
                            EMAIL               TEXT    NOT NULL);''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS CATEGORIES
                            (ID     INT PRIMARY KEY     NOT NULL,
                            NAME                TEXT    NOT NULL,
                            ABOUT               TEXT    NOT NULL,
                            START_TIME          TEXT    NOT NULL);''')

    def commit(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Commits changes to the Database\n
            To be used with the GUI"""

        self.conn.commit()

    def closeDB(self):
        """ Author: Alex Lambert\n
            UWnetID: alamb25\n
            Date: 3/7/17\n
            Closes the database\n
            DOES NOT COMMIT CHANGES!"""

        self.conn.close()

    def addContestant(self, entry):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Add contestant to the Database"""

        newID = random.randint(10000, 99999)
        while newID in self.usedIDs:
            newID = random.randint(10000, 99999)
        entry.insert(0, newID)
        self.cursor.execute("INSERT INTO CONTESTANTS VALUES (?, ?, ?, ?)", entry)

    def getContestant(self, userID):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Gets contestant from the Database using unique user ID"""

        temp = self.cursor.execute('SELECT * FROM CONTESTANTS WHERE USERID=?', (userID,))
        toReturn = []
        for entry in temp:
            toReturn.append(entry[0])
            toReturn.append(entry[1])
            toReturn.append(entry[2])
            toReturn.append(entry[3].split('/'))
        return toReturn

    def getAllContestants(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Returns all contestants from the Database"""

        toReturn = []
        temp = self.cursor.execute('SELECT * FROM CONTESTANTS')

        for entry in temp:
            tmp = entry[3].split('/')
            toReturn.append([entry[0], entry[1], entry[2], tmp])
        return toReturn

    def getAllContestantUserIDs(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Returns all contestants' unique userIDs from the Database"""

        toReturn = []
        temp = self.cursor.execute('SELECT USERID FROM CONTESTANTS').fetchall()

        for entry in temp:
            toReturn.append(entry[0])
        return toReturn

    def modifyContestant(self, userID, categories):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Modifies existing Contestant using the unique userID\n
            Changes the contestant's categories list"""

        temp = [categories, userID]
        self.cursor.execute('UPDATE CONTESTANTS set CATEGORIES=? where USERID=?', temp)

    def removeContestant(self, userID):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Removes the contestant corresponding to the unique userIDs from the Database\n
            Used for when a contestant gets moved to being a Judge"""

        self.conn.execute("DELETE FROM CONTESTANTS WHERE USERID=?", (userID,))

    def addJudge(self, entry):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Adds the judge to the database"""

        newID = random.randint(10000, 99999)
        while newID in self.usedIDs:
            newID = random.randint(10000, 99999)
        entry.insert(0, newID)
        self.cursor.execute("INSERT INTO JUDGES VALUES (?, ?, ?, ?)", entry)

    def getJudge(self, userID):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Returns the judge from the Database using the unique id"""

        temp = self.cursor.execute('SELECT * FROM JUDGES WHERE USERID=?', (userID,))
        toReturn = []
        for entry in temp:
            toReturn.append(entry[0])
            toReturn.append(entry[1])
            toReturn.append(entry[2])
            toReturn.append(entry[3].split('/'))
        return toReturn

    def getAllJudges(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Returns all judges from the Database"""

        toReturn = []
        temp = self.cursor.execute('SELECT * FROM JUDGES')

        for entry in temp:
            tmp = entry[3].split('/')
            toReturn.append([entry[0], entry[1], entry[2], tmp])
        return toReturn

    def getAllJudgesUserIDs(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Returns all judges' unique userIDs from the Database"""

        toReturn = []
        temp = self.cursor.execute('SELECT USERID FROM JUDGES').fetchall()

        for entry in temp:
            toReturn.append(entry[0])
        return toReturn

    def modifyJudge(self, userID, categories):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Modifies existing Judge using the unique userID\n
            Changes the judge's categories list"""

        temp = [categories, userID]
        self.cursor.execute('UPDATE JUDGES set CATEGORIES=? where USERID=?', temp)

    def removeJudge(self, userID):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Removes the judge from the Database"""

        self.conn.execute("DELETE FROM JUDGES WHERE USERID=?", (userID,))

    def addAdmin(self, entry):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Adds the admin to the database
            USED FOR HARDCODED"""

        newID = random.randint(10000, 99999)
        while newID in self.usedIDs:
            newID = random.randint(10000, 99999)
        entry.insert(0, newID)
        self.cursor.execute("INSERT INTO ADMINS VALUES (?, ?, ?)", entry)

    def getAdmin(self, userID):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Returns the Admin from the Database using the unique id"""

        temp = self.cursor.execute('SELECT * FROM ADMINS WHERE USERID=?', (userID,))
        toReturn = []
        for entry in temp:
            toReturn.append(entry[0])
            toReturn.append(entry[1])
            toReturn.append(entry[2])
        return toReturn

    def getAllAdmins(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Returns all Admins from the Database
            Might not be used"""

        toReturn = []
        temp = self.cursor.execute('SELECT * FROM ADMINS')

        for entry in temp:
            toReturn.append([entry[0], entry[1], entry[2]])
        return toReturn

    def getAllAdminsUserIDs(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Returns all judges' unique userIDs from the Database"""

        toReturn = []
        temp = self.cursor.execute('SELECT USERID FROM ADMINS').fetchall()

        for entry in temp:
            toReturn.append(entry[0])
        return toReturn

    def removeAdmin(self, userID):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Removes the judge from the Database
            Might not be used"""

        self.conn.execute("DELETE FROM ADMINS WHERE USERID=?", (userID,))

    def addCategorie(self, entry):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Add Categorie to the Database"""

        newID = random.randint(10000, 99999)
        while newID in self.usedIDs:
            newID = random.randint(10000, 99999)
        entry.insert(0, newID)
        self.cursor.execute("INSERT INTO CATEGORIES VALUES (?, ?, ?, ?)", entry)

    def getCategorie(self, id):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Gets the Categorie from the Database using unique user ID"""

        temp = self.cursor.execute('SELECT * FROM CATEGORIES WHERE ID=?', (id,))
        toReturn = []
        for entry in temp:
            toReturn.append(entry[0])
            toReturn.append(entry[1])
            toReturn.append(entry[2])
            toReturn.append(entry[3])
        return toReturn

    def getAllCategories(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Returns all Categories from the Database"""

        toReturn = []
        temp = self.cursor.execute('SELECT * FROM CATEGORIES')

        for entry in temp:
            toReturn.append([entry[0], entry[1], entry[2], entry[3]])
        return toReturn

    def getAllCategoriesIDs(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Returns all Categories' unique IDs from the Database"""

        toReturn = []
        temp = self.cursor.execute('SELECT ID FROM CATEGORIES').fetchall()

        for entry in temp:
            toReturn.append(entry[0])
        return toReturn

    def modifyCategorie(self, id, newEntry):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Modifies existing Categorie using the unique ID\n"""
        # newEntry.insert(0, id)
        # temp = [categories, userID]
        self.cursor.execute("UPDATE CATEGORIES set NAME=? where ID=?", [newEntry[0], id])
        self.cursor.execute("UPDATE CATEGORIES set ABOUT=? where ID=?", [newEntry[1], id])
        self.cursor.execute("UPDATE CATEGORIES set START_TIME=? where ID=?", [newEntry[2], id])


    def removeCategorie(self, id):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Removes the categorie corresponding to the unique userIDs from the Database\n"""

        self.conn.execute("DELETE FROM CATEGORIES WHERE ID=?", (id,))
    
    
    