from User import *

"""Contestant class"""
class Contestant(User):
    """Contestant class"""

    def __init__(self):
        """Constructor"""

        #Category array

        #Create contestant
        self = User("Bobby", "bobbob@uderwaterbasketweaving.com")

        #Add contestant to database
        temp = [self.userID, self.name, self.email, ""] #Modified by Alex 3/7/17
        self.database.addContestant(temp)               #Fixed how contestants are added to db

        #Print contestant info
        a = self.database.getContestant(self.userID)
        for x in a:
            print x

    def regCategory(self):
        """Registers contestant in chosen category"""
        pass

    def dropCategory(self):
        """Drops contestant from chosen category"""

        #Modify internal list
        #Send userID and modified list
        
        pass


"""Main"""
if __name__ == '__main__':
    test = Contestant()


