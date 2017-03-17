import sqlite3
import random

class Database(object):

    """ Author: Alex Lambert\n
        UW NetID: alamb25\n
        Date: 3/7/17\n
        Database object that holds information about events"""

    def __init__(self, dbName='Database.db'):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Constructor"""

        self.conn = sqlite3.connect(dbName)
        self.cursor = self.conn.cursor()
        self.intializeTables()
        self.idList = (self.getAllContestantUserIDs() +
                       self.getAllJudgesUserIDs() +
                       self.getAllAdminsUserIDs() +
                       self.getAllCategoriesIDs())


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

    def doesUserExist(self, userID):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/9/17\n
            Checks the database if the user exists
            returns 1 if contestant, 2 for judge and 3 for admin, 0 if none exist"""

        toReturn = 0
        temp = self.getContestant(userID)
        if temp != []:
            currentUser = userID 
            toReturn = 1
        temp = self.getJudge(userID)
        if temp != []:
            toReturn = 2
        temp = self.getAdmin(userID)
        if temp != []:
            toReturn = 3

        return toReturn

    def addContestant(self, entry):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Add contestant to the Database
            Returns the unique id"""

        newID = random.randint(10000, 99999)
        while newID in self.idList:
            newID = random.randint(10000, 99999)

        entry.insert(0, newID)
        self.idList.append(newID)
        entry[3] = '/'.join(entry[3])
        self.cursor.execute("INSERT INTO CONTESTANTS VALUES (?, ?, ?, ?)", entry)

        return newID

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

        if userID in self.idList:
            self.conn.execute("DELETE FROM CONTESTANTS WHERE USERID=?", (userID,))
            self.idList.remove(userID)

    def addJudge(self, entry, userID=0):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Adds the judge to the database"""

        if userID < 10000:
            newID = random.randint(10000, 99999)
            while newID in self.idList:
                newID = random.randint(10000, 99999)
            entry.insert(0, newID)
            userID = newID

        entry[3] = '/'.join(entry[3])
        self.idList.append(userID)
        self.cursor.execute("INSERT INTO JUDGES VALUES (?, ?, ?, ?)", entry)

        return userID

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
        if userID in self.idList:
            self.conn.execute("DELETE FROM JUDGES WHERE USERID=?", (userID,))
            self.idList.remove(userID)

    def addAdmin(self, entry):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Adds the admin to the database
            USED FOR HARDCODING ONLY"""
        self.idList.append(entry[0])
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
        if userID in self.idList:
            self.conn.execute("DELETE FROM ADMINS WHERE USERID=?", (userID,))
            self.idList.remove(userID)

    def addCategory(self, entry):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Add Category to the Database"""

        newID = random.randint(10000, 99999)
        while newID in self.idList:
            newID = random.randint(10000, 99999)
        entry.insert(0, newID)
        self.idList.append(newID)
        self.cursor.execute("INSERT INTO CATEGORIES VALUES (?, ?, ?, ?)", entry)

        return newID

    def getCategory(self, id):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Gets the Category from the Database using unique user ID"""

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

    def modifyCategory(self, id, newEntry):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Modifies existing Category using the unique ID\n"""

        self.cursor.execute("UPDATE CATEGORIES set NAME=? where ID=?", [newEntry[0], id])
        self.cursor.execute("UPDATE CATEGORIES set ABOUT=? where ID=?", [newEntry[1], id])
        self.cursor.execute("UPDATE CATEGORIES set START_TIME=? where ID=?", [newEntry[2], id])


    def removeCategory(self, id):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Removes the category corresponding to the unique userIDs from the Database\n"""

        if id in self.idList:
            self.conn.execute("DELETE FROM CATEGORIES WHERE ID=?", (id,))
            self.idList.remove(id)
