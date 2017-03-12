from Database import *

if __name__ == '__main__':
    db = Database()
    temp = db.getAllContestants()
    for row in temp:
        print row[0], row[1], row[2], ' '.join(row[3])
