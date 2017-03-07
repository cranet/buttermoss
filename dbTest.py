from Database import *


#Tests functions of Database.py
if __name__ == '__main__':

    testDB = Database()
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
    temp = testDB.getAllContestant()
    for row in temp:
        print row[0], row[1], row[2], ' '.join(row[3])

    print '\n===GET ALL IDs TEST TEST==='
    temp = testDB.getAllContestantuserID()
    for row in temp:
        print row

    print '\n===REMOVE TEST==='
    testDB.removeContestant(12345)
    temp = testDB.getAllContestant()
    for row in temp:
        print row[0], row[1], row[2], ' '.join(row[3])


