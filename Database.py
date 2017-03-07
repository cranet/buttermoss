import sqlite3
import os

class Database(object):

    def __init__(self):

        self.conn = sqlite3.connect('example.db')
        self.cursor = self.conn.cursor()
        if not os.path.isfile('example.db'):
            self.intializeTables()

    def intializeTables(self):
        self.cursor.execute('''CREATE TABLE CONTESTANTS
                            (ID INT PRIMARY KEY     NOT NULL,
                            NAME            TEXT    NOT NULL,
                            EMAIL           TEXT    NOT NULL,
                            CATEGORIES      TEXT    NOT NULL);''')
        self.cursor.execute('''CREATE TABLE JUDGES
                            (ID INT PRIMARY KEY     NOT NULL,
                            NAME            TEXT    NOT NULL,
                            EMAIL           TEXT    NOT NULL,
                            CATEGORIES      TEXT    NOT NULL);''')
        self.cursor.execute('''CREATE TABLE ADMINS
                            (ID INT PRIMARY KEY     NOT NULL,
                            NAME            TEXT    NOT NULL,
                            EMAIL           TEXT    NOT NULL);''')
        self.cursor.execute('''CREATE TABLE CATEGORIES
                            (ID INT PRIMARY KEY     NOT NULL,
                            NAME            TEXT    NOT NULL,
                            ABOUT           TEXT    NOT NULL,
                            START_TIME      TEXT    NOT NULL);''')
        # self.cursor.execute('''CREATE TABLE contestants
        #                    (id INTEGER, name text, email text, categories text);''')
        # self.cursor.execute('''CREATE TABLE judges
        #                    (id INTEGER, name text, email text, categories text)''')
        # self.cursor.execute('''CREATE TABLE admins
        #                    (id INTEGER, name text, email text)''')
        # self.cursor.execute('''CREATE TABLE categories
        #                    (id INTEGER, name text, about text, startTime text)''')

    def commit(self):
        self.conn.commit()

    def addContestant(self, id, name, email, categories):
        thing = [id, name, email, categories]
        self.cursor.execute("INSERT INTO CONTESTANTS (ID,NAME,EMAIL,CATEGORIES) \
                            VALUES (?, ?, ?, ?)", thing)

    def getContestant(self, id):
        toReturn = self.cursor.execute('SELECT * FROM CONTESTANTS WHERE ID=?', (id,))
        return toReturn

    def getAllContestant(self):
        toReturn = self.cursor.execute('SELECT * FROM CONTESTANTS')
        return toReturn

    def getAllContestantID(self):
        return set(self.cursor.execute('SELECT id FROM contestants').fetchall())

    def modifyContestant(self, id, t):
        catList = " ".join(t)
        te = [catList, id]
        self.cursor.execute('UPDATE set categories=? where id=?', te)

    def removeContestant(self, id):
        self.conn.execute("DELETE FROM contestants WHERE id=?", (id,))

    def addJudge(self, id, name, email, categories):
        thing = [id, name, email, categories]
        self.cursor.execute("INSERT INTO contestants VALUES (?, ?, ?, ?)", thing)

    def getJudge(self, id):
        self.cursor.execute('SELECT id, name, email, categories FROM contestants WHERE id=?', (id,))
        return self.cursor.fetchone()

    def removeJudge(self, id):
        self.conn.execute("DELETE FROM contestants WHERE id=?", (id,))

    def closeDB(self):
        self.conn.close()
