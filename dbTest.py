import os
from Database import *

def testContestantDB(testDB):
    """ Test the Contestant Databse functions"""

    testDB.addContestant(['Toad', 'cranet@uw.edu', 'NONE'])
    testDB.addContestant(['Alex', 'alamb25@uw.edu', 'NONE/ONE/TWO'])
    testDB.addContestant(['Caleb', 'caleb447@uw.edu', 'NONE/TWO'])

    print '\n===GET ALL CONTESTANT IDs TEST==='
    temp = testDB.getAllContestantUserIDs()
    tmp = 0
    for row in temp:
        print row
        tmp = row

    print '\n===GET CONTESTANT TEST==='
    temp = testDB.getContestant(tmp)
    print temp[0], temp[1], temp[2], temp[3][0]

    print '\n===MODIFY CONTESTANT TEST==='
    testDB.modifyContestant(tmp, 'NONE/THREE')
    temp = testDB.getContestant(tmp)
    print temp[0], temp[1], temp[2], ' '.join(temp[3])

    print '\n===GET ALL CONTESTANT TEST==='
    temp = testDB.getAllContestants()
    for row in temp:
        print row[0], row[1], row[2], ' '.join(row[3])

    print '\n===REMOVE CONTESTANT TEST==='
    testDB.removeContestant(tmp)
    temp = testDB.getAllContestants()
    for row in temp:
        print row[0], row[1], row[2], ' '.join(row[3])

def testJudgeDB(testDB):
    """ Test the Judge Databse functions"""

    testDB.addJudge(['Toad', 'cranet@uw.edu', 'NONE'])
    testDB.addJudge(['Alex', 'alamb25@uw.edu', 'NONE/ONE/TWO'])
    testDB.addJudge(['Caleb', 'caleb447@uw.edu', 'NONE/TWO'])

    print '\n===GET ALL JUDGE IDs TEST==='
    temp = testDB.getAllJudgesUserIDs()
    for row in temp:
        print row
        tmp = row

    print '\n===GET JUDGE TEST==='
    temp = testDB.getJudge(tmp)
    print temp[0], temp[1], temp[2], temp[3][0]

    print '\n===MODIFY JUDGE TEST==='
    testDB.modifyJudge(tmp, 'NONE/THREE')
    temp = testDB.getJudge(tmp)
    print temp[0], temp[1], temp[2], ' '.join(temp[3])

    print '\n===GET ALL JUDGES TEST==='
    temp = testDB.getAllJudges()
    for row in temp:
        print row[0], row[1], row[2], ' '.join(row[3])

    print '\n===GET ALL JUDGE IDs TEST==='
    temp = testDB.getAllJudgesUserIDs()
    for row in temp:
        print row

    print '\n===REMOVE JUDGE TEST==='
    testDB.removeJudge(tmp)
    temp = testDB.getAllJudges()
    for row in temp:
        print row[0], row[1], row[2], ' '.join(row[3])

def testCategoryDB(testDB):
    """ Test the CATEGORY Databse functions"""

    testDB.addCategory(['Toad Contesy', 'fun', '9:30am'])
    testDB.addCategory(['Alex Contest', 'more fun', '10:30am'])
    testDB.addCategory(['Caleb Contest', 'less fun', '11:45am'])

    print '\n===GET ALL CATEGORIES IDs TEST==='
    temp = testDB.getAllCategoriesIDs()
    for row in temp:
        print row
        tmp = row

    print '\n===GET CATEGORY TEST==='
    temp = testDB.getCategory(tmp)
    print temp[0], temp[1], temp[2], temp[3]

    print '\n===MODIFY CATEGORY TEST==='
    testDB.modifyCategory(tmp, ['Under Water Basket Weaving', 'even more fun', '12:30pm'])
    temp = testDB.getCategory(tmp)
    print temp[0], temp[1], temp[2], temp[3]

    print '\n===GET ALL CATEGORY TEST==='
    temp = testDB.getAllCategories()
    for row in temp:
        print row[0], row[1], row[2], row[3]

    print '\n===REMOVE CATEGORY TEST==='
    testDB.removeCategory(tmp)
    temp = testDB.getAllCategories()
    for row in temp:
        print row[0], row[1], row[2], row[3]

def testAdminDB(testDB):
    """ Test the Admin Databse functions"""

    testDB.addAdmin(['Toad', 'cranet@uw.edu'])
    testDB.addAdmin(['Alex', 'alamb25@uw.edu'])
    testDB.addAdmin(['Caleb', 'caleb447@uw.edu'])

    print '\n===GET ALL ADMINS IDs TEST==='
    temp = testDB.getAllAdminsUserIDs()
    for row in temp:
        print row
        tmp = row

    print '\n===GET ADMIN TEST==='
    temp = testDB.getAdmin(tmp)
    print temp[0], temp[1], temp[2]

    print '\n===GET ALL ADMINS TEST==='
    temp = testDB.getAllAdmins()
    for row in temp:
        print row[0], row[1], row[2]

    print '\n===REMOVE ADMIN TEST==='
    testDB.removeAdmin(tmp)
    temp = testDB.getAllAdmins()
    for row in temp:
        print row[0], row[1], row[2]

#Tests functions of Database.py
if __name__ == '__main__':
    db = Database('Demo.db')
    testContestantDB(db)
    testJudgeDB(db)
    testAdminDB(db)
    testCategoryDB(db)
    #close and get rid of database
    db.closeDB()
    try:
        os.remove('Demo.db')
    except OSError:
        pass

