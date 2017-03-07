from Database import *

def testContestantDB(testDB):
    """ Test the Contestant Databse functions"""

    testDB.addContestant([12345, 'Toad', 'cranet@uw.edu', 'NONE'])
    testDB.addContestant([11025, 'Alex', 'alamb25@uw.edu', 'NONE/ONE/TWO'])
    testDB.addContestant([24581, 'Caleb', 'caleb447@uw.edu', 'NONE/TWO'])

    print '\n===GET CONTESTANT TEST==='
    temp = testDB.getContestant(12345)
    print temp[0], temp[1], temp[2], temp[3][0]

    print '\n===MODIFY CONTESTANT TEST==='
    testDB.modifyContestant(12345, 'NONE/THREE')
    temp = testDB.getContestant(12345)
    print temp[0], temp[1], temp[2], ' '.join(temp[3])

    print '\n===GET ALL CONTESTANT TEST==='
    temp = testDB.getAllContestants()
    for row in temp:
        print row[0], row[1], row[2], ' '.join(row[3])

    print '\n===GET ALL CONTESTANT IDs TEST==='
    temp = testDB.getAllContestantUserIDs()
    for row in temp:
        print row

    print '\n===REMOVE CONTESTANT TEST==='
    testDB.removeContestant(12345)
    temp = testDB.getAllContestants()
    for row in temp:
        print row[0], row[1], row[2], ' '.join(row[3])

def testJudgeDB(testDB):
    """ Test the Judge Databse functions"""

    testDB.addJudge([12345, 'Toad', 'cranet@uw.edu', 'NONE'])
    testDB.addJudge([11025, 'Alex', 'alamb25@uw.edu', 'NONE/ONE/TWO'])
    testDB.addJudge([24581, 'Caleb', 'caleb447@uw.edu', 'NONE/TWO'])

    print '\n===GET JUDGE TEST==='
    temp = testDB.getJudge(12345)
    print temp[0], temp[1], temp[2], temp[3][0]

    print '\n===MODIFY JUDGE TEST==='
    testDB.modifyJudge(12345, 'NONE/THREE')
    temp = testDB.getJudge(12345)
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
    testDB.removeJudge(12345)
    temp = testDB.getAllJudges()
    for row in temp:
        print row[0], row[1], row[2], ' '.join(row[3])

#Tests functions of Database.py
if __name__ == '__main__':
    db = Database()
    testContestantDB(db)
    testJudgeDB(db)


